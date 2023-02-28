from itertools import product
from django.shortcuts import render,redirect
from django.http import HttpResponse
from customer.models import Mycart
from homecommon.models import Customer
from django.db.models import F

from seller.models import Product

# Create your views here.
def cus_home(request):
    prod_list=Product.objects.all()
    return render(request,'cus_templates/cus_home.html',{'prod_data':prod_list})

def product_detail(request,pid):
    msg=''
    product = Product.objects.get(id=pid)
    if request.method =='POST':
        quantity=request.POST['qty']
        product_exist=Mycart.objects.filter(product=pid,customer=request.session['customer']).exists()
        print(product_exist)
        if not product_exist:
            item = Mycart(customer_id = request.session['customer'],product_id = pid,quantity = quantity)
            item.save()
        else:  
            msg = 'Item already added'
            
    # context = {
    #     'product_details':product,
    #     'msg':msg
    # }
    return render (request, 'cus_templates\product_detail.html',{'product_details':product,'msg':msg})


def mycart(request):  
    # cart_datas=Mycart.objects.get(customer_id=request.session['customer'])
    cartdata=Mycart.objects.filter(customer_id=request.session['customer']).annotate(total=F('product__Product_price')*F('quantity'))
    # cart_data=Mycart.objects.annotate(total=F('product__Product_price')*F('quantity'))
    grand_total=0
    for i in cartdata:

        grand_total=i.total+grand_total
        request.session['grand']=grand_total
    context={
           'data':cartdata,
            'grandtotal':grand_total
                            }
    return render(request,'cus_templates/mycart.html',context)

def myorder(request):
    return render(request,'cus_templates/myorder.html')

def edit_profile(request):
    if request.method == 'POST':
        edt_name = request.POST['editprofile_name']
        edt_address = request.POST['editprofile_address']
        edt_mobile = request.POST['editprofile_mobile']
        edt_email = request.POST['editprofile_email']
        edt_gender = request.POST['editprofile_gender']

    
        updt = Customer.objects.filter(id = request.session['customer']).update(customer_name = edt_name,
            address = edt_address,
            mobile = edt_mobile,
            email = edt_email,
            gender = edt_gender)
        # editcustomer.save(id = request.session['customer'])
    return render(request,'cus_templates/edit_profile.html')

def change_pass(request):
    return render(request,'cus_templates/change_pass.html')

def cus_profile(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'cus_templates/cus_profile.html',{'data':customer_details})

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('homecommon:home')


def delete_item(request,pid):
    cart_item=Mycart.objects.get(id=pid)
    cart_item.delete()
    cartdata=Mycart.objects.filter(customer_id=request.session['customer'])
    cart_data=Mycart.objects.annotate(total=F('product__Product_price')*F('quantity'))
    return render(request,'cus_templates/mycart.html',{'data':cart_data})


    