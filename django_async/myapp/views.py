from django.shortcuts import render
from django.http import HttpResponse
from time import sleep

import asyncio

import httpx


# Create your views here.

# 异步任务

# 同步任务

# 异步视图

# 同步视图


async def index(request):
    return HttpResponse('<h1 style="text-align: center; margin-top: 300px;">Hello Django async</h1>')
