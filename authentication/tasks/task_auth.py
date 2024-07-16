from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.conf import settings
from time import sleep
import sys


@shared_task
def send_otp_to_user(id) : 
    sleep(2)
    user = get_user_model().objects.get(id=id)
    # context = {"code":user.otp}
    # content = render_to_string("send_email.html",context=context) 
    # email = EmailMultiAlternatives(
    #     from_email=settings.EMAIL_HOST_USER,
    #     to=[user.email],
    #     subject="activation code"
    # )
    # email.attach_alternative(content,"text/html")
    # email.send()
    sys.stdout.write(user.otp)
    sleep(120)
    user = get_user_model().objects.get(id=id)
    if not user.is_active : 
        user.delete()
    else : 
        user.save()