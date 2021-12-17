from django.contrib import auth
from django.contrib.auth import forms
from django.contrib.auth.models import User
from django.http.response import HttpResponse
from django.http import HttpResponseRedirect , JsonResponse
from django.urls import reverse
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm 
from django.contrib import messages
from django.contrib.auth.views import PasswordChangeView
from .models import Profile
from .forms import ProfileForm
from django.shortcuts import get_object_or_404, render 
from shop.views import *
from orders.models import OrderItem
from django.urls import reverse_lazy
from django.contrib.auth import login, authenticate, logout
from django.core.mail import EmailMessage
# Create your views here.

def SignupView(request):
    if request.method == "POST":

        try:
       
            un = request.POST["uname"]    
            pwd = request.POST["password"]   
            #fn = request.POST["first_n"]
        
            usr = User.objects.create_user(username = un,password = pwd)
            usr.is_staff = True
            #usr.first_name = fn
            #usr.password = pwd
            #usr.username = un
            #usr.save()       
         
        
            reg = Profile(user=usr )
        
            reg.save()
            return render(request ,'accounts/succes.html')
        except:
            messages.error(request, 'نام کاربری تکراری یا فرمت کلمه عبور اشتباه میباشد.')
            
    return render(request ,'accounts/signup.html')


    


def LoginView(request):
    # اگر رکوئست با متد POST ارسال شده بود یعنی کاربر فرم لاگین را سابمیت کرده است
    if request.method == 'POST':
        # از متد user.authemticate برای یافتن کاربر استفاده میشود. این متد یه متغیر از نوع آبجکت user بر می گرداند
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        # چک می کند که اگر متغیر یوزر خالی نبود، لاگین را با اطلاعات یوزر انجام دهد
        if user is not None:
            auth.login(request, user)
            # در اینجا کاربر را به صفحه ای که میخواهیم پس از لاگین به وی نمایش دهیم ریدایرکت می کنیم
            return render(request ,'accounts/profile.html')
        # در صورتی که متغیر یوزر خالی بود
        # یعنی کاربر با مشخصاتی که در فرم وارد شده است وجود ندارد
        else:
            # کاربر را به همراه یک پیام خطا به صفحه لاگین باز می گرداند
            # این پیغام خطا در قسمت تعبیه شده در بالای صفحه لاگین به نمایش در می آید
            messages.error(request, 'نام کابری یا کلمه عبور اشتباه میباشد.')
            return render(request, 'accounts/login.html')
            
    # اگر رکوئست با متد GET ارسال شده بود یعنی کاربر لینک صفحه لاگین را زده و میخواهد صفحه لاگین را ببیند
    else:
        return render(request, 'accounts/login.html')






def logout(request):
    auth.logout(request)
    res =  HttpResponseRedirect("/")
    res.delete_cookie("user_id")
    res.delete_cookie("date_login")
    return res
    #return render(request ,'accounts/login.html')







def edit_profile(request):

   context = {}
   data = Profile.objects.get(user__id = request.user.id)
   context["data"] = data
   if request.method =="POST":
       print(request.POST)
       fn = request.POST["first_name"]
       ln = request.POST["last_name"]
       nc = request.POST["national_code"]
       mn = request.POST["mobile_number"]
       em = request.POST["email"]
       pn = request.POST["pay_number"]
       
       
       data.first_name =fn
       data.last_name = ln
       data.national_code = nc
       data.mobile_number = mn
       data.email = em
       data.pay_number = pn
       data.save()

       if "image" in request.FILES:
           img = request.FILES["image"]
           data.profile_image = img
           data.save()

       context["Status"] = "changed save"


   return render(request ,'accounts/profile.html' , context)



def Order_History(request):
    itemss = OrderItem.objects.filter(user = request.user)
    context = {
      'itemss': itemss,
    }
    return render(request ,'accounts/profile.html' , context)
    
    
def change_password(request):
    context={}
    ch = Profile.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = Profile.objects.get(user__id=request.user.id)
        context["data"] = data
    if request.method=="POST":
        current = request.POST["cpwd"]
        new_pas = request.POST["npwd"]
        
        user = User.objects.get(id=request.user.id)
        un = user.username
        check = user.check_password(current)
        if check==True:
            user.set_password(new_pas)
            user.save()
            user = User.objects.get(username=un)
            login(request,user)
   

    return render(request,"accounts/profile.html",context)
   

def sendemail(request):
    context = {}
    ch = Profile.objects.filter(user__id=request.user.id)
    if len(ch)>0:
        data = Profile.objects.get(user__id=request.user.id)
        context["data"] = data

    if request.method=="POST":
    
        rec = request.POST["to"].split(",")
        print(rec)
        sub = request.POST["sub"]
        msz = request.POST["msz"]

        try:
            em = EmailMessage(sub,msz,to=rec)
            em.send()
            context["status"] = "Email Sent"
            context["cls"] = "alert-success"
        except:
            context["status"] = "Could not Send, Please check Internet Connection / Email Address"
            context["cls"] = "alert-danger"
    return render(request,'accounts/sendemail.html',context  )

def forgotpass(request):
    context = {}
    if request.method=="POST":
        un = request.POST["username"]
        pwd = request.POST["npass"]

        user = get_object_or_404(User,username=un)
        user.set_password(pwd)
        user.save()

        login(request,user)
        if user.is_superuser:
            return HttpResponseRedirect("/admin")
        else:
          context["status"] = "Password Changed Successfully!!!"

    return render(request,'accounts/forgot_pass.html',context)

import random

def reset_password(request):
    un = request.GET["username"]
    try:
        user = get_object_or_404(User,username=un)
        otp = random.randint(1000,9999)
        msz = "Dear {} \n{} is your One Time Password (OTP) \nDo not share it with others \nThanks&Regards \nMyWebsite".format(user.username, otp)
        try:
            email = EmailMessage("Account Verification",msz,to=[user.email])
            email.send()
            return JsonResponse({"status":"sent","email":user.email,"rotp":otp})
        except:
            return JsonResponse({"status":"error","email":user.email})
    except:
        return JsonResponse({"status":"failed"})