from config import celery_app
from django.core.mail import send_mail
from .models import Order


@celery_app.task
def send_mail_with_order(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order #{order.id}'
    message = f'You have successfully placed an order.' \
              f'Your order ID is {order.id}'
    mail_sent = send_mail(subject, message, 'admin@mail.ru', [order.user.email])
    return mail_sent
