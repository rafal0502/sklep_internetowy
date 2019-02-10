from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Zadanie wysyłające powiadomienie za pomocą wiadomości e-mail po zakończonym
    powodzeniem utworzeniu obiektu zamówienia.
    :param order_id:
    :return:
    """
    order = Order.objects.get(id=order_id)
    subject = f'Zamówienie nr {order_id}'
    message = f'Witaj, {order.first_name}!\n\Złożyłeś zamówienie w naszym sklepie.\'' \
        f'Identyfikator zamówienia to {order.id}.'
    mail_sent = send_mail(subject, message, 'rafalchojnacki0502@gmail.com', [order.email])
    return mail_sent

