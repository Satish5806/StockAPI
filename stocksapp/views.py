from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import StockSerializer,StockPriceSerializer
from .models import Stock, StockPrice

# Create your views here.
class StocksView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


