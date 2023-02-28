from django.shortcuts import render,redirect

from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings



import random

from homecommon.models import Customer,Seller

# Create your views here.


def home(request):
    return render(request,'commontemplates/home.html')

def customer_login(request):
    msg=''
    if request.method=="POST":
        cust_mail=request.POST['c_mail']
        cust_pass=request.POST['c_pass']
        try:
            customer=Customer.objects.get(e_mail=cust_mail,password=cust_pass)
            request.session['customer']=customer.id
            return redirect('customer:cus_home')
        except:
            msg="Invalid emailid or password!!!!"
    return render(request,'commontemplates/customer_login.html',{'msg':msg})

def email_exist(request):
    # email is a variable to store value of emailid given in customer registration
    email=request.POST['emailid']
# e_mail is the name give for the table in database ,checks this value is equal to the value is input box of email if exits or not this value
# is passed to status and then given to registration page to display
    status=Customer.objects.filter(e_mail=email).exists()
    return JsonResponse({'status':status})

def customer_registration(request):
    if request.method=='POST':
        cust_name=request.POST['c_name']
        cust_gender=request.POST['c_gender']
        cust_phone=request.POST['c_phone']
        cust_mail=request.POST['c_mail']
        cust_add=request.POST['c_add']
        cust_pass=request.POST['c_pass']
        cust_img=request.FILES['c_img']
        new_customer=Customer(
            customer_name=cust_name,
            gender=cust_gender,
            ph_number=cust_phone,
            e_mail=cust_mail,
            address=cust_add,
            password=cust_pass,
            image=cust_img
                    
        )
        new_customer.save()
    return render(request,'commontemplates/customer_registration.html')


def seller_reg(request):
    if request.method=='POST':
        sel_name=request.POST['s_seller_name']
        sel_com_name=request.POST['s_com_name']
        sel_add=request.POST['s_address']
        sel_mobile=request.POST['s_mobileno']
        sel_email=request.POST['s_email']
        sel_com_logo=request.FILES['s_com_logo']
        sel_bank_name=request.POST['s_bank_name']
        sel_bankholder=request.POST['s_hol_name']
        sel_acc_no=request.POST['s_acc_no']
        sel_ifsc=request.POST['s_ifsc']
        sel_branch_name=request.POST['s_branch_name']
        sel_username=random.randint(1111,9999)
        sel_password= 'sel-' + sel_name.lower()+ str(sel_username)
        message='Hi your username is' + str(sel_username) + 'and temporary password is' + sel_password 

        new_seller=Seller(
            seller_name= sel_name,
            company_name=sel_com_name,
            address=sel_add,
            mobile=sel_mobile,
            e_mail=sel_email,
            company_logo=sel_com_logo,
            bank_name=sel_bank_name,
            acc_name=sel_bankholder,
            accc_no=sel_acc_no,
            ifsc=sel_ifsc,
            branch_name=sel_branch_name,
            Username=sel_username,
            password=sel_password,
        )

       
        send_mail(
            'username and temporry password ',
            message,
            settings.EMAIL_HOST_USER,
            # ['sel_email'], use this code if not using default emailid
            # here we set mailid for all seller as default 

            ['23project2023@gmail.com'],
            fail_silently = False
            )
        new_seller.save()     
    return render(request,'commontemplates/seller_reg.html')

def seller_login(request):
    msg=''
    if request.method=="POST":
        uusername=request.POST['s_mail']
        ppassword=request.POST['s_pass']
        try:
            seller=Seller.objects.get(Username=uusername,password=ppassword)
            request.session['seller']=seller.id
            return redirect('seller:sel_home')
        except:
            msg="Invalid emailid or password!!!!"
    return render(request,'commontemplates/seller_login.html')




