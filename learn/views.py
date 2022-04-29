from contextlib import redirect_stderr
import re
from telnetlib import STATUS
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound
# Create your views here.

def my_view(request):
    a=2
    if a==1:
        return HttpResponseNotFound('<h1>Page not found</h1>')
    elif a==2:
        return HttpResponse(status=499)
    else:
        return HttpResponse('<h1>Page  found</h1>')

def index(request):
    return render(request,'learn/index.html')   #渲染页面

