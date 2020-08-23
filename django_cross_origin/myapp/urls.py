from django.urls import path

from myapp import views

app_name = 'myapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('demo-1/', views.demo_1, name='demo-1')
]
