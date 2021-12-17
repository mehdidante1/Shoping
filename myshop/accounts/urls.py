from django.urls import path
from .views import  *
from django.contrib.auth.views import PasswordResetView , PasswordResetDoneView , PasswordResetConfirmView , PasswordResetCompleteView 
from .forms import *
app_name = 'accounts'


urlpatterns = [
    path('login/' , LoginView , name = 'login'),
    path('reset_password/' , reset_password , name = 'reset_password'),
    path('logout/', logout, name = 'logout'),
    path('edit_profile/', edit_profile, name = 'edit_profile'),
    path('register/',SignupView , name = 'register'),
    path('Order_History/',Order_History , name = 'Order_History'),
    path("change_password/",change_password,name="change_password"),
    path("sendemail/",sendemail, name="sendemail"),
    path("forgotpass/",forgotpass, name="forgotpass"),
    path("reset_password/",reset_password,name="reset_password"),


    path('password_reset/',
         PasswordResetView.as_view(
                template_name = 'accounts/reset_password.html',
                form_class = MyPassResetForm
         ), 
         name='password_reset'),
    
    path('password_reset/done/',
         PasswordResetDoneView.as_view(
                template_name = 'accounts/password_reset_done.html'
         ), 
         name='password_reset_done'),
    
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
              template_name = 'accounts/password_reset_confirm.html',
              form_class = MySetPassForm
         ), 
         name='password_reset_confirm'),
    

    path('password_reset/complete',
         PasswordResetCompleteView.as_view(
                template_name = 'accounts/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
]
