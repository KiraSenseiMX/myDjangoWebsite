from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

def index(request):
    absoluteurl = request.build_absolute_uri()
    return render(request, 'marketplaceApp/index.html', {
        'absoluteurl':absoluteurl
    })