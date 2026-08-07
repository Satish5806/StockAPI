from rest_framework import serializers
from .models import Stock, StockPrice, Watchlist
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) #To hide password in the response
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    #This below function is the method to create token for login 
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = ['symbol', 'sector', 'name', 'created_at']
    

class StockPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockPrice
        fields = ['stock', 'date', 'open', 'close', 'high', 'low', 'volume']


class WatchlistSerializer(serializers.ModelSerializer):
    stock = StockSerializer(read_only=True)
    stock_id = serializers.PrimaryKeyRelatedField(
            queryset = Stock.objects.all(), source='stock', write_only=True
        )
    class Meta:
        model = Watchlist
        fields = ['user', 'stock','stock_id', 'created_at']
        read_only_fields = ['user', 'created_at']