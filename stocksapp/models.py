from django.db import models
from datetime import datetime, date
from django.contrib.auth import get_user_model
from django.db.models import constraints

# Create your models here.
User = get_user_model()


class Stock(models.Model):
    symbol = models.CharField(max_length=20)
    sector = models.CharField(max_length=20)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.symbol

class StockPrice(models.Model):
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    open = models.DecimalField(max_digits=10, decimal_places=2)
    close = models.DecimalField(max_digits=10, decimal_places=2)
    high = models.DecimalField(max_digits=10, decimal_places=2)
    low = models.DecimalField(max_digits=10, decimal_places=2)
    volume = models.IntegerField()

    def __str__(self):
        return f'{self.stock.symbol}-{self.date}'


class Watchlist(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='watchlists')
    stock = models.ForeignKey(Stock, on_delete=models.CASCADE, related_name='watched_by')
    created_at = models.DateTimeField(auto_now_add= True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['user', 'stock'],
                name='unique_user_stock',
            )
        ]

    def __str__(self):
        return f'{self.user.username}-{self.stock.symbol}'
