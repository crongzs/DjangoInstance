from django.urls import path

from app import views


app_name = 'app'

urlpatterns = [
    path('hello/', views.ProfileAPIView.as_view(), name='hello')
]