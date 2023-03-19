from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'protectlinkApp/index.html')

def unlock_view(request):
    return render(request, 'protectlinkApp/unlock.html')