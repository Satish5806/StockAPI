from rest_framework import serializers
from .models import Stock, StockPrice

class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['symbol', 'sector', 'name', 'created_at']

class StockPriceSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    class Meta:
        model = StockPrice
        fields = ['stock', 'date', 'open', 'close', 'high', 'low', 'volume']
        