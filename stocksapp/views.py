import logging
from rest_framework.generics import ListAPIView,  ListCreateAPIView, RetrieveAPIView, CreateAPIView
from .serializer import RegisterSerializer, StockSerializer,StockPriceSerializer, WatchlistSerializer
from .models import Stock, StockPrice, Watchlist
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
# Create your views here.
logger = logging.getLogger(__name__)

class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        logger.info(
            f"Registration request of {request.data.get('username', 'unknown')} received."
        )
        return super().post(request, *args, **kwargs)


class StocksView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['sector']
    search_fields = ['symbol', 'name']
    ordering_fields = ['name', 'created_at']

    def get(self, request, *args, **kwargs):
        logger.info(
            (f'{request.user.username} viewed the stock list')
        )
        return super().get(request, *args, **kwargs)


class StockDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'symbol'

    def get(self, request, *args, **kwargs):
        logger.info(f"Stock {kwargs['symbol']} was accessed")
        return super().get(request, *args, **kwargs)



class StockPriceView(ListAPIView):
    queryset = StockPrice.objects.all()

    def get_queryset(self):
        symbol = self.kwargs.get('symbol')
        if  not symbol :
            return StockPrice.objects.none()
        logger.info(f'{self.request.user.username} viewed price history of {symbol}.')
        return StockPrice.objects.filter(stock__symbol = symbol)
    
    serializer_class = StockPriceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['date']


class WatchlistView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WatchlistSerializer

    def get_queryset(self): 
        return Watchlist.objects.filter(user = self.request.user).order_by('created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        logger.info(
            f'{self.request.user.username} added {serializer.instance.stock.symbol} to the watchlist'
        )


    



