'''
pip install django==2.2.*      安装
django-admin startproject web  创建一个项目
cd web                         进入目录
python manage.py runserver     启动服务
    Performing system checks...
    System check identified no issues (0 silenced).
    You have 17 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
    Run 'python manage.py migrate' to apply them.
    October 05, 2021 - 15:28:46
    Django version 2.2.24, using settings 'web.settings'
    Starting development server at http://127.0.0.1:8000/
    Quit the server with CTRL-BREAK.
此时访问127.0.0.1:8000 就可以访问

python manage.py startapp 应用名   ：创建应用
'''

'''
创建一个应用名叫myhome，访问/时显示hello world
python manage.py startapp myhome 
1. 在创建的应用中，写view函数   myhome/view.py
视图函数，输出hello world
    views.py
        from django.shortcuts import render
        from django.http import HttpResponse
            def index(request):
            return HttpResponse('hello word')
2. 给当前应用指定路由        myhome/urls.py,子路由文件
    from django.contrib import admin
    from django.urls import path
    from . import views
    urlpatterns = [
        path('', views.index),    #当访问/时就路由到view文件的index
    ]

3. 在跟路由配置当前应用   web/urls.py
    from django.contrib import admin
    from django.urls import path,include
    import myhome

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('',include('myhome.urls'))
    ]
python manage.py runserver 重新启动服务 此时
'''

'''
项目结构名词
    路由
        定义用户访问url和相应视图函数的映射
    视图
        一个函数或方法，也可以定义成类
        接受用户请求并响应
        项目中主要逻辑代码在视图函数中
    模板
        在django框架中，有一个模板引擎，可以做到将html和python逻辑代码分离
        并在视图函数中需要给用户响应模板时，返回或传递数据
    模型
        专门处理数据
        在django框架中，通过定义一个模型类，来实现对数据库中数据进行操作
        在开发中，对类中的数据进行操作，会映射到数据库，转化为sql执行
    静态文件
'''

'''
框架设计模式
    MVC设计
    M Model  模型--->数据管理
    V View   视图--->页面展示
    C Controller 控制器--->逻辑代码
    
    django设计模式  MVT
    M  模型-->数据层管理
    V  视图-->逻辑层管理，代码，流程控制
    T  模板-->模板管理，页面展示
核心思想：
    将逻辑代码，数据控制，页面展示完全分离
    降低程序模块间耦合
'''