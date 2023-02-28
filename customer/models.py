from django.db import models

from homecommon.models import Customer
from seller.models import Product

# Create your models here.
# ADD TO CART
# PRODUCT 
# CUSTOMER 
# QUTY (INT OR BIGINT)
class Mycart(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    quantity=models.BigIntegerField()
    