from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_name=models.CharField(max_length=50)
    gender=models.CharField(max_length=20)
    ph_number=models.CharField(max_length=20)
    e_mail=models.CharField(max_length=100)
    address=models.CharField(max_length=500)
    password=models.CharField(max_length=16)
    image=models.ImageField(upload_to='customer/')

# by default table name is defined as appname with class name.above table name will be homecommonCustomer. to change table name use the code 
# given below then table name will be customer.then makemigrations and migrate
    class Meta:
        db_table='customer'

class Seller(models.Model):
    seller_name=models.CharField(max_length=100)
    company_name=models.CharField(max_length=200)
    address=models.CharField(max_length=500)
    mobile=models.CharField(max_length=20)
    e_mail=models.CharField(max_length=100)
    company_logo=models.ImageField(upload_to='seller/')
    bank_name=models.CharField(max_length=150)
    acc_name=models.CharField(max_length=150)
    accc_no=models.BigIntegerField()
    ifsc=models.CharField(max_length=150)
    branch_name=models.CharField(max_length=500)
    Username=models.CharField(max_length=100)
    password=models.CharField(max_length=16)


