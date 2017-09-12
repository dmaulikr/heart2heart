from celery import shared_task
from celery.decorators import periodic_task
from celery.task.schedules import crontab
from django.core.mail import send_mail

@shared_task
def add(x, y):
    return x + y

@periodic_task(run_every=(crontab(minute='*/1')))
def sendmeemail():
    send_mail(
        "This is an automated email from yours faithfully",
        "Sent with love from heart2heart project using celery periodic task ",
        'tegaesabunor@gmail.com',
        ['tesabunor@gmail.com'],
        fail_silently=False,
    )