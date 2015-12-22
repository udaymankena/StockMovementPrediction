from django.db import models
from django.utils import timezone
# Create your models here.
class CompTweets(models.Model):
    company = models.CharField(max_length=50)
    tweet = models.CharField(max_length=140)

class StockTable(models.Model):
    date = models.DateField(default=timezone.now)
    open = models.DecimalField(max_digits=5,decimal_places=2)
    high = models.DecimalField(max_digits=5,decimal_places=2)
    low = models.DecimalField(max_digits=5,decimal_places=2)
    close = models.DecimalField(max_digits=5,decimal_places=2)
    company = models.CharField(max_length=50,default='Apple')