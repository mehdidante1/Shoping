from django.forms.fields import EmailField
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render 
from .models import Category, Comments, Product , Product_mobile
from cart.forms import CartAddProductForm
from .forms import CommentForm
from django.contrib import messages

def product_list(request, category_slug=None , category_slug2= None,category_slug3=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    productss = Product.objects.filter(available=True)
    product_mobile = Product_mobile.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if category_slug2:
        category2 = get_object_or_404(Category, slug=category_slug)
        product_mobile = product_mobile.filter(category=category2)

    if category_slug3:
        category = get_object_or_404(Category, slug=category_slug3)
        productss= productss.filter(category=category)


    context = {
        'categories': categories,
        "category": category,
        "products": products,
        "productss": product_mobile,
        "productsss": productss
        } 
    return render (request,'shop/product/base.html', context) 






def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True )
    cart_product_form = CartAddProductForm
    comments = Comments.objects.all().filter(product = product , available=True)
    is_favourite = False
    if product.favourite.filter(id=request.user.id).exists():
        is_favourite = True
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_email = form.cleaned_data["email"]
            new_massage = form.cleaned_data["massage"]

            new_comment = Comments(product = product ,name=new_name , email = new_email , massage = new_massage)
            new_comment.save()
            messages.success(request, 'نظر شما با موفقیت ثبت شد.')
    context = {
        'is_favourite' : is_favourite,
        'product':product,
        'form':cart_product_form,
        'commentss':comments,
    }
    
    return render(request,"shop/product/detail.html",context ) 


def product_mobile(request, id, slug):
    product2 = get_object_or_404(Product_mobile ,id=id, slug=slug, available=True )
    context = {
        'product2':product2,
    }
    
    return render(request,"shop/product/detail_mobile.html",context ) 

    

    
def favourite_post(request , id):
    post = get_object_or_404(Product,id=id)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
    else:
        post.favourite.add(request.user)
    return HttpResponseRedirect(post.get_absolute_url())

def post_favourite_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts' : favourite_posts,   
    }
    return render(request , 'accounts/profile.html' , context)