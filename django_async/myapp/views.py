from django.shortcuts import render
from django.http import HttpResponse
from time import sleep

import asyncio

import httpx


# Create your views here.


# 异步试图
async def index(request):
    return HttpResponse('<h1 style="text-align: center; margin-top: 300px;">Hello Django async</h1>')


# 异步任务
async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org/")
        print(r)


# 同步任务
def http_call_sync():
    for n in range(1, 6):
        sleep(1)
        print(n)
    r = httpx.get("https://httpbin.org/")
    print(r)


# 异步视图调用异步任务
async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


# 同步视图调用同步任务
def sync_view(request):
    http_call_sync()
    return HttpResponse("Blocking HTTP request")
