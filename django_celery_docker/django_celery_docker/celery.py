import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_docker.settings')

app = Celery('django_celery_docker', backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
