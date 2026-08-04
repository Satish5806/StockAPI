from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StockSerializer,StockPriceSerializer
from .models import Stock, StockPrice

# Create your views here.
class StocksView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer

class StockDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = 'symbol'

class StockPriceView(ListAPIView):
    queryset = StockPrice.objects.all()
    serializer_class = StockPriceSerializer



