from .models import OrderItem

def item(request):
    items = OrderItem.objects.all()
    return{'items':items}