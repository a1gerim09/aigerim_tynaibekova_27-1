from django.shortcuts import HttpResponse
from datetime import datetime
import pytz


def hello(request):
    return HttpResponse("Hello! It's my project")


def now_date(request):
    timezone = pytz.timezone("Asia/Bishkek")
    now = datetime.now(timezone)
    return HttpResponse(now)


def goodbye(request):
    return HttpResponse("Goodbye user!")



