'''该文件用于路由选择'''
from django.contrib import admin
from django.urls import path
from . import views
import myhome

urlpatterns = [
    # path('', views.index),    #当访问/时就路由到view文件的index
    path('love',views.love),   #当访问love时路由到view文件love函数
    path('',views.test_templates)
]