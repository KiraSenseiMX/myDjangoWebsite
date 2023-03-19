from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    absoluteurl = request.build_absolute_uri()
    return render(request, 'protectlinkApp/index.html', {
        'absoluteurl':absoluteurl
    })

def unlock_view(request):
    return render(request, 'protectlinkApp/unlock.html')