from django.urls import path, include
from .views import StockDetailView, StockPriceView, StocksView

urlpatterns = [
    path('stocks/', StocksView.as_view(), name='stock'),
    path('stocks/<str:symbol>/', StockDetailView.as_view(), name='stock_detail'),
    path('stocks/<str:symbol>/prices/', StockPriceView.as_view(), name= 'stock_price')
]