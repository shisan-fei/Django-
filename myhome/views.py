import re
from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def index(request):
    # return HttpResponse('欢迎访问…………')
    return render(request,'aa/index.html')

def love(request):
    return HttpResponse('i love you si mi da')

def test_templates(request):
    return render(request,'aa/index.html')

def deam(request):
    #添加数据,方法1
    # obj=models.stu()
    # obj.name = 'wlf'
    # obj.age=21
    # obj.sex = '男'
    # obj.address='陕西'
    # obj.save()     #save是stu继承models类的方法,此时添加完数据，当再次访问deam时，就会将数据添加到数据库myhome_stu
    # print(obj.save())
    #方法2
    data = {'name':'李四','age':22,'sex':'男','address':'石家庄'}
    obj = models.stu(**data)
    obj.save()
    return HttpResponse('模型测试链接')