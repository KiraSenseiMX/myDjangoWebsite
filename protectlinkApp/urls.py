from django.urls import path

from . import views

app_name = 'protectlinkApp'
urlpatterns = [
    path(       '', views.index,       name='index' ),
    path('unlock/', views.unlock_view, name='unlock'),
]