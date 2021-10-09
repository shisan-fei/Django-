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
    # data = {'name':'王五','age':23,'sex':'男','address':'南天门'}
    # obj = models.stu(**data)
    # obj.save()
    
    #获取数据所有
    # data = models.stu.objects.all()      #object是stu的方法
    # print(data)                          #data是对象集，通过对象集可以读取对应数据
    # for i in data:
    #     print(i.name)
        
    #通过字段获取数据对象
    # obj=models.stu.objects.get(id=2)   #获取id为2的对象
    # obj=models.stu.objects.filter(age=23)   #获取age为23的对象，没有或有多个时使用filter就不会报错
    # print(obj,obj.name)                 #输出对象那个值-->stu object (2) 李四
    
    #删除数据
    # obj = models.stu.objects.get(id=2)
    # obj.delete()
     
    #修改数据
    obj = models.stu.objects.get(id=3)   #将id为3的name改为老三
    # obj = models.stu.objects.last() #最后一个
    obj.name='老三'
    obj.save()
    
    return HttpResponse('模型测试链接')