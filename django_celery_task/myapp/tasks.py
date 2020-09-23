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
