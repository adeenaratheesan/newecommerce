from django.urls import path 
from.import views
app_name='customer'

urlpatterns=[
   path('cus_home/',views.cus_home,name='cus_home'),
   path('product_detail/<int:pid>',views.product_detail,name='product_detail'),
   path('myorder/',views.myorder,name='myorder'),
   path('cus_profile/',views.cus_profile,name='cus_profile'),
   path('mycart/',views.mycart,name='mycart'),
   path('change_pass/',views.change_pass,name='change_pass'),
   path('logout/',views.logout,name='logout'),
   path('edit_profile/',views.edit_profile,name='edit_profile'),
   path('delete_item/<int:pid>',views.delete_item,name='delete_item'),

]
