from django.urls import path

from . import views

app_name = 'qrcodegeneratorApp'
urlpatterns = [
    path('', views.index, name='index'),
]