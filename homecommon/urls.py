from django.urls import path
from .import views
app_name='homecommon'

urlpatterns=[
   path('customer_login/',views.customer_login,name='customer_login'),
   path('customer_registration/',views.customer_registration,name='customer_registration'),
   path('home/',views.home,name='home'),
   path('seller_login/',views.seller_login,name='seller_login'),
   path('seller_reg/',views.seller_reg,name='seller_reg'),
   path('email_exist/',views.email_exist,name='email_exist'),
   
  
]