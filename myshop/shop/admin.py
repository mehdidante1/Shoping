from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Category)
class Categoryadmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

    @admin.register(Product)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug', 'price', 'available', 'updated']
        list_filter = ['available', 'created', 'updated']
        list_editable = ['price', 'available', ]
        prepopulated_fields = {'slug': ('name',)}


    @admin.register(Product_mobile)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ['name', 'slug', 'price', 'available', 'updated']
        list_filter = ['available', 'created', 'updated']
        list_editable = ['price', 'available', ]
        prepopulated_fields = {'slug': ('name',)}    

    

    @admin.register(Comments)
    class ProductAdmin(admin.ModelAdmin):
        list_display = ['name', 'email', 'massage', 'available']
        list_filter = ['available', 'date']
        list_editable = ['available',]
      
admin.site.register(Cartt)
admin.site.register(CartProduct)
admin.site.register(Orderr)
admin.site.register(ProductImage)