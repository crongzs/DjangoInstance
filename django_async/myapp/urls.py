from django.urls import path

from myapp import views

app_name = 'myapp'

urlpatterns = [
    # 异步试图
    path('', views.index, name='index'),
    path('async-view', views.async_view, name='async-view'),

    # 同步试图
    path('sync-view', views.sync_view, name='sync-view'),
]
