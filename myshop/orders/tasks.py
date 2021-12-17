from celery import shared_task
from django.core.mail import send_mail
from .models import Order



@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f"your order {order.id}"
    massage = f"dear {order.first_name}.your order is ready"
    mail_sent = send_mail(subject,massage, "mehdimosavi@gmail.com",[order.email])
    return mail_sent




