from django.urls import path 
from.import views
app_name='seller'

urlpatterns=[
   path('sel_home/',views.sel_home,name='sel_home'),
   path('product_catelogue/',views.product_catelogue,name='product_catelogue'),
   path('add_product/',views.add_product,name='add_product'),
   path('change_pass/',views.change_pass,name='change_pass'),
   path('sel_profile/',views.sel_profile,name='sel_profile'),
   path('sel_home/',views.sel_home,name='sel_home'),
   path('recent_orders/',views.recent_orders,name='recent_orders'),
   path('update_stock/',views.update_stock,name='update_stock'),
   path('order_his/',views.order_his,name='order_his'),
]