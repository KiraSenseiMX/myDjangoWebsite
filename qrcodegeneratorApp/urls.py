from django.urls import path

from . import views

app_name = 'qrcodegeneratorApp'
urlpatterns = [
    path('qrcodegenerator', views.index, name='index'),
]