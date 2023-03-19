"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

#from django.conf.urls import url
#from django_js_reverse.views import urls_js

urlpatterns = [
    path('admin/', admin.site.urls),
    path('protectlink', include('protectlinkApp.urls')),
    path('wewillreturnat', include('wewillreturnatApp.urls')),
    path('qrcodegenerator', include('qrcodegeneratorApp.urls')),
    path('', include('homeApp.urls')),
    #url(r'^jsreverse/$', urls_js, name='js_reverse'),
    path('myapp/', include('myapp.urls')),
]
