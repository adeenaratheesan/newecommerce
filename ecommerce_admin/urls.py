from django.urls import path 
from.import views
app_name='ecommerce_admin'

urlpatterns=[
   path('ad_login/',views.ad_login,name='ad_login'),
   path('approve_seller/',views.approve_seller,name='approve_seller'),
   path('view_seller/',views.view_seller,name='view_seller'),
   path('admin_home/',views.admin_home,name='admin_home'),
   path('index/',views.index,name='index'),


]