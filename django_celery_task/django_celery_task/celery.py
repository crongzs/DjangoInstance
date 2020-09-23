import os

from celery import Celery
from celery.schedules import crontab

from django.conf import settings

from datetime import timedelta

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_celery_task.settings')

app = Celery('django_celery_task', backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Periodic Tasks
app.conf.beat_schedule = {
    # 每10秒运行task.add任务。
    'add-every-30-seconds': {
        'task': 'myapp.tasks.add',
        'schedule': 10.0,
        'args': (16, 16)
    },
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'myapp.tasks.email',
        'schedule': crontab(hour=7, minute=30, day_of_week=1),
        'args': (16, 16),
    },
}

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
