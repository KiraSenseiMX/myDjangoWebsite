from django.urls import path

from . import views

app_name = 'marketplaceApp'
urlpatterns = [
    path('', views.index, name='index'),
]