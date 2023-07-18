from django.core.mail import send_mail
from django.contrib.auth.models import User
import dramatiq
from datetime import timedelta
from django.utils.timezone import now
from django.contrib.auth.models import User
from dramatiq import get_broker


@dramatiq.actor
def send_greetings_email():
    users = User.objects.all()

    for user in users:
        subject = 'Привет'
        message = f'Привет, {user.username}!'
        from_email = 'testdevdjango@fastmail.com'
        recipient_list = [user.email]

        send_mail(subject, message, from_email, recipient_list)

send_greetings_email.send_with_options(delay=600000)