from hw_12.celery import app
from django.core.mail import send_mail


@app.task
def my_send_mail(email, remind):
    send_mail('REMINDER',
              f'{remind}',
              'orlov229003@gmail.com',
              [email],
              fail_silently=False
              )
