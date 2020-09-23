from django.shortcuts import render
from django.http import HttpResponse

from .tasks import test


# Create your views here.

def index(request):
    test.delay('触发异步任务')
    return HttpResponse('<h1>Hello Django Celery</h1>')
