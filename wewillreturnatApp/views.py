from django.shortcuts import render

from django.http import HttpResponse
import datetime

# Create your views here.

def monthNumber2text(monthNumber):
    monthText = ['Jan', 'Feb', 'Mar', 'Apr',
                 'May', 'Jun', 'Jul', 'Aug',
                 'Sep', 'Oct', 'Nov', 'Dec',
                ]
    return monthText[monthNumber-1]

def dayNumber2text(dayNumber):
    str_dayNumber = str(dayNumber)
    str_unitsDigit = str_dayNumber[len(str_dayNumber)-1]

    if(str_unitsDigit == '1'):
        return f'{dayNumber}st'
    elif(str_unitsDigit == '2'):
        return f'{dayNumber}nd'
    elif(str_unitsDigit == '3'):
        return f'{dayNumber}rd'
    else:
        return f'{dayNumber}th'


def index(request):

    datetime_now = datetime.datetime.now()

    now = {
        # force 2, 4 or 6 digits and fill with zeros
        'year': f'{datetime_now.year:04}',
        'month': monthNumber2text(datetime_now.month),
        'day': dayNumber2text(datetime_now.day),
        'hour': f'{datetime_now.hour:02}',
        'minute': f'{datetime_now.minute:02}',
        'second': f'{datetime_now.second:02}',
        # just keep the 2 most significant digits
        'microsecond': f'{datetime_now.microsecond:06}'[:2],
    }

    context = {
        'now': now,
        'deadline': '???',
    }

    return render(request, 'wewillreturnatApp/index.html', context)
