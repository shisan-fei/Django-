import re
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello word')

def love(request):
    return HttpResponse('i love you si mi da')