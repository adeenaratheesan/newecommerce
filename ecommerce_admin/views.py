from django.shortcuts import redirect, render
from django.http import HttpResponse
import ecommerce_admin
from rest_framework.response import Response
from rest_framework.decorators import api_view

from homecommon.models import Seller

# Create your views here.
def ad_login(request):
     msg =""
     if request.method == 'POST':
        admin_username = request.POST['a_username']
        admin_password = request.POST['a_password']
        try:
            admin_data = ecommerce_admin.objects.get(username = admin_username, password = admin_password)
            request.session['admin'] = admin_data.id
            return redirect('ecom_admin:admin_home')
        except:
            msg = 'invalid username or password'

    
     return render(request,'admin_templates/ad_login.html',{'message':msg})



def approve_seller(request):
    return render(request,'admin_templates/approve_seller.html')

def view_seller(request):
    return render(request,'admin_templates/view_seller.html')

def admin_home(request):
    return render(request,'admin_templates/admin_home.html')

def view_seller(request):
    seller_details = Seller.objects.all()
    return render(request,'admin_templates/view_seller.html',{'sel_details':seller_details})

@api_view(['GET'])
def index(request):
    message='congratulations, you have created an API'
    return Response(message)

