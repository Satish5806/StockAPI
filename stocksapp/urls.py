from django.urls import path, include
from .views import StockDetailView, StockPriceView, StocksView, RegisterView, WatchlistView

urlpatterns = [
    path('stocks/', StocksView.as_view(), name='stock'),
    path('stocks/<str:symbol>/', StockDetailView.as_view(), name='stock_detail'),
    path('stocks/<str:symbol>/prices/', StockPriceView.as_view(), name= 'stock_price'),
    path('register/', RegisterView.as_view(), name = 'register_user'),
    path('watchlist/', WatchlistView.as_view(), name = 'stock_watchlist')
]