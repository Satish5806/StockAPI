from rest_framework.request import Request
from rest_framework.generics import ListAPIView,  ListCreateAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from .serializer import RegisterSerializer, StockSerializer,StockPriceSerializer, WatchlistSerializer
from .models import Stock, StockPrice, Watchlist
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer

class StocksView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ['sector']
    search_fields = ['symbol', 'name']
    ordering_fields = ['name', 'created_at']


class StockDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'symbol'

class StockPriceView(ListAPIView):
    queryset = StockPrice.objects.all()
    def get_queryset(self):
        symbol = self.kwargs.get('symbol')
        if  not symbol :
            return StockPrice.objects.none()
        return StockPrice.objects.filter(stock__symbol = symbol)
    serializer_class = StockPriceSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_fields = ['date']

class WatchlistView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]

    def get_queryset(self): 
        return Watchlist.objects.filter(user = self.request.user)
    serializer_class = WatchlistSerializer

    def perform_create(self, serializer):
            serializer.save(user=self.request.user)


    



