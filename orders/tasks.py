from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """ Wysyła wiadomość po udanej transakcji """

    order = Order.objects.get(id=order_id)
    subject = 'Zamówienie nr {}'.format(order.id)
    message = 'Witaj, {}!\n\zZłożyłeś zamówienie w naszym sklepie'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message, 'admin@myshop.co', [order.email])
    return mail_sent