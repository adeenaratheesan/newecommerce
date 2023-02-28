from django.shortcuts import render
from django.http import HttpResponse

from homecommon.models import Seller
from seller import models
from seller.models import Product




# Create your views here.

def product_catelogue(request):
    product_details=Product.objects.filter(seller_id=request.session['seller'])
    return render(request,'sel_templates/product_catelogue.html',{'data':product_details})

def add_product(request):
    if request.method=='POST':
        # pseller=request.POST['']
        pname=request.POST['s_pname']
        pnum=request.POST['s_pid']
        pdescription=request.POST['s_pdescription']
        pstock=request.POST['s_pstock'] 
        pprice=request.POST['s_pprice']
        pimg=request.FILES['s_pimg']
        new_product=Product(
            seller_id= request.session['seller'],
            product_name= pname,
            product_num=pnum,
            description=pdescription,
            product_stock= pstock,
            Product_price=pprice,
            image= pimg,   
        )
       
        new_product.save()
    return render(request,'sel_templates/add_product.html')

def change_pass(request):
    return render(request,'sel_templates/change_pass.html')

def sel_profile(request):
    seller_details = Seller.objects.get(id = request.session['seller'])
    return render(request,'sel_templates/sel_profile.html',{'data':seller_details})

def sel_home(request):
    seller_data =Seller.objects.get(id=request.session['seller'])
    return render(request,'sel_templates/sel_home.html',{'data':seller_data})

def recent_orders(request):
    return render(request,'sel_templates/recent_orders.html')

def update_stock(request):
    return render(request,'sel_templates/update_stock.html')

def order_his(request):
    return render(request,'sel_templates/order_his.html')





