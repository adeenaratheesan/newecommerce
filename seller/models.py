
from django.db import models

from homecommon.models import Seller



# Create your models here.
class Product(models.Model):
    seller=models.ForeignKey(Seller,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=50)
    product_num=models.CharField(max_length=20)
    description=models.CharField(max_length=500)
    product_stock=models.BigIntegerField()
    Product_price=models.FloatField()
    image=models.ImageField(upload_to='product/')
    category = models.CharField(max_length=100,default='')