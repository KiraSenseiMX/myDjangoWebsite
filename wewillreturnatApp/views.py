from django.shortcuts import render

from django.http import HttpResponse
import datetime

# Create your views here.

def index(request):

    print("---------------------------------------------")

    # testing the datetime lib

    now = datetime.datetime.now()
    print(now)

    year = now.year
    month = now.month
    day = now.day
    print(year, month, day)

    hour = now.hour
    minute = now.minute
    print(hour, minute)

    print("---------------------------------------------")

    return render(request, 'wewillreturnatApp/index.html')