from django.shortcuts import render
from .models import *
from django.http import HttpResponse, JsonResponse
import datetime
from datetime import timedelta
from django.conf import settings
import os

BASE_DIR = settings.BASE_DIR
result_path = os.path.join(BASE_DIR, 'app/result.txt')
result_path2 = os.path.join(BASE_DIR, 'app/result2.txt')


# Create your views here.

def Homepage(request):
    return HttpResponse('Homepage')


def Result(request):
    print(result_path)
    f = open(result_path, "r")
    Ans = eval(f.read())
    return JsonResponse({'result': Ans})


def Result2(request):
    print(result_path2)
    f = open(result_path, "r")
    Ans = eval(f.read())
    return JsonResponse({'result': Ans})
