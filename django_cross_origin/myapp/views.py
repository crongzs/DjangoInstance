from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


def index(request):
    return HttpResponse('<h1>Hello World</h1>')


def demo_1(request):
    ''' 返回一个json数据 '''
    return JsonResponse(["Hello World", "Hello Django"], safe=False)
