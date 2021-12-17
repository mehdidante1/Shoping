from django.db import models
from shop.models import Product
from django.contrib.auth.models import User
# Create your models here.


class Order(models.Model):
    
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email =  models.EmailField( max_length=254)
    national_code = models.IntegerField()
    name_of_receiver = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    postal_address = models.CharField(max_length=200)
    postal_code = models.CharField( max_length=50)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'#سفارش {self.id}'


class OrderItem(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    order = models.ForeignKey(Order,related_name='items',on_delete=models.CASCADE)
    product = models.ForeignKey(Product,related_name='order_items' , on_delete=models.CASCADE)
    price = models.PositiveIntegerField()
    quantity = models.PositiveIntegerField(default=1)
    

    def __str__(self): 
        return str(self.id)

    
    def get_cost(self):
        return self.price * self.quantity
