from django import forms
from django.db import models
from django.forms import fields
from .models import Order



class OrderCreateform(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['first_name' , 'last_name' , 'email' , 'national_code', 'name_of_receiver' , 'phone_number' ,'postal_address' , 'postal_code' , 'city']
        