from celery import Celery 
import os 

os.environ.setdefault("DJANGO_SETTINGS_MODULE","core.settings")

app = Celery("songsara")
app.config_from_object("django.conf:settings",namespace="CELERY")

app.autodiscover_tasks()