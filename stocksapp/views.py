from rest_framework.generics import ListAPIView, RetrieveAPIView
from .serializer import StockSerializer,StockPriceSerializer
from .models import Stock, StockPrice
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class StocksView(ListAPIView):
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


