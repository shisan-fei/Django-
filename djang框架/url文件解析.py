'''
from django.contrib import admin
from django.urls import path,include,re_path

import myhome

urlpatterns = [
    path('admin/', admin.site.urls),    path('匹配条件',西培成功后访问的视图)
    path('',include('myhome.urls')),
    re_path('^love$',views.love)          re_path可以匹配正则
]
'''
from django.contrib import admin
from django.urls import path,include,re_path

# urlpatterns = [
#     path('articles/<int:year>',views.love),    #可以匹配参数year，要给视图函数传入该参数,类型可以传入int str等
#     re_path('^abc/([0-9]{3})/$',views.love)    #视图函数传入函数
#     path('abc/123',views.love,name='myhome_love')  #给路由起个名字
# ]


