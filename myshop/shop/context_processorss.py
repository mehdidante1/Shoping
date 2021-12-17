from .models import Product 

def product(request):
    products = Product.objects.all()
    return{'products':products}
