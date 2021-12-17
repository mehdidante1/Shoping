from django import forms
from django.contrib.auth import models
from django.contrib.auth.forms import PasswordResetForm , SetPasswordForm
from .models import Profile
class LoginForm(forms.Form):
        username = forms.CharField()
        password = forms.CharField(widget=forms.PasswordInput)


class BootstrapStyleMixin:
    field_names = None


    def __init__(self , *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.field_names:
            for fieldname in self.field_names:
                self.fields[fieldname].widget.attrs = {'class': 'form-control'}
        else:
            raise ValueError('The field_names must be set')

class MyPassResetForm(BootstrapStyleMixin , PasswordResetForm):
    field_names = ['email']


class MySetPassForm(BootstrapStyleMixin , SetPasswordForm):
    field_names = ['new_password1' , 'new_password2']

class ProfileForm(forms.Form):

    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=150)
    national_code = forms.CharField(max_length=40)
    mobile_number = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=200)
    pay_number = forms.CharField(max_length=100)
    profil_image = forms.ImageField()


  


