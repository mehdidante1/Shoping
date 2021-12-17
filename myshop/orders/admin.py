from django.contrib import admin
from .models import OrderItem , Order
# Register your models here.


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id' , 'first_name' , 'last_name' , 'email' , 'national_code' , 'name_of_receiver' , 'phone_number' , 'postal_address' , 'city' , 'created' , 'updated' , 'paid']
    list_fillter = ('paid' , 'created' , 'updated')
    inlines = [OrderItemInline]