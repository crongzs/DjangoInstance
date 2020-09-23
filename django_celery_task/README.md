# Django Celery

setting.py
~~~python
INSTALLED_APPS = [
    ...,
    'myapp',
    'django_celery_results',
    'django_celery_beat',
]
# Celery
BROKER_TRANSPORT_OPTIONS = {'visibility_timeout': 43200}  # 设置超时时间，一定要设置

# CELERY_BACKEND = 'redis://127.0.0.1:6379/3'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_BROKER = 'redis://127.0.0.1:6379/4'
CELERY_TIMEZONE = 'Asia/Shanghai'
CELERY_ENABLE_UTC = True
~~~

celery.py
~~~python
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
~~~

__init__.py
~~~python
from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
from .celery import app as celery_app

__all__ = ('celery_app',)
~~~

myapp/tasks.py
~~~python
from celery import shared_task
import time


@shared_task
def test(arg1):
    print(arg1)
    time.sleep(10)
    print('执行异步任务')
    return 'ok'


@shared_task
def add(a, b):
    print('执行定时任务add')
    return a + b


@shared_task
def email(a, b):
    print('执行定时任务email')
    return a + b
~~~

myapp/views.py
~~~python
from django.shortcuts import render
from django.http import HttpResponse

from .tasks import test


# Create your views here.

def index(request):
    test.delay('触发异步任务')
    return HttpResponse('<h1>Hello Django Celery</h1>')
~~~

> start
~~~bash
// 只用异步任务
celery -A django_celery_task worker -l info
// 不使用django_celery_baet scheduler 调度
celery -A django_celery_task worker -B -l info
// 使用django_celery_baet scheduler 调度
celery -A django_celery_task beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
~~~
## 使用Django ORM/Cache作为结果存储

~~~bash
pip install django-celery-results
~~~

~~~python
INSTALLED_APPS = (
    ...,
    'django_celery_results',
)
~~~

~~~bash
python manage.py migrate django_celery_results
~~~

### 结果存储

1. database
~~~python
CELERY_RESULT_BACKEND = 'django-db'
~~~
2. catch
~~~python
CELERY_CACHE_BACKEND = 'django-cache'

# celery setting.
CELERY_CACHE_BACKEND = 'default'

# django setting.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}
~~~

~~~bash
celery -A proj worker -l info
~~~


## 使用自定调度类
~~~bash
$ pip install django-celery-beat
~~~

~~~python
INSTALLED_APPS = (
    ...,
    'django_celery_beat',
)
~~~

~~~bash
python manage.py migrate
~~~

~~~bash
celery -A proj beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
~~~