from django.conf.urls import url
from django.urls import path
from .import views 

app_name= "shop"


urlpatterns = [

    path("",views.product_list,name="product_list"),
    path("<slug:category_slug>",views.product_list,name="product_list_by_category"),
    path("<int:id>/<slug:slug>/",views.product_detail,name="product_detail"),
    path("<int:id>/<slug:slug>/",views.product_mobile,name="product_mobile"),
    path(r'(?P<id>\d+)/favourite_post/$',views.favourite_post , name ="favourite_post"),
    path(r'favourites/$',views.post_favourite_list , name ="post_favourite_list"),

   
]
