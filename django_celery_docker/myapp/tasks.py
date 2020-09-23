from celery import shared_task
import time
from datetime import date




@shared_task
def test(arg1):
    print(arg1)
    time.sleep(5)
    today = date.today()
    print('执行异步任务')
    log_path = '/django_celery_docker/celery_{}.log'.format(today)
    with open(log_path, 'a') as f:
        f.write('执行异步任务\n')
    return 'ok'
