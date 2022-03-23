from django.db import models
from django.conf import settings

#一对一外键   ForeignKey。一下是引用外键的三种情况。
class Manufacturer(models.Model):
    # 定义一个模型，存放汽车生产厂商
    pass

class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)  #ForeignKey字段（to, on_delete, **options）

#2 如果你要关联的模型位于当前模型之后，则需要通过字符串的方式进行引用
class Car(models.Model):
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.CASCADE)   #引用Manufacturer变成字符串

class Manufacturer(models.Model):
    # 定义一个模型，存放汽车生产厂商
    pass

#3 假设Manufacturer模型存在于production这个app中
class Car(models.Model):
    manufacturer = models.ForeignKey(
        'production.Manufacturer',         # 关键在这里！！
        on_delete=models.CASCADE,
    )


#on_delete参数，在Django2.0之后，不可以省略了。
'''
on_delete=参数
CASCADE 模拟SQL语言中的ON DELETE CASCADE约束 将定义有外键的模型对象同时删除
PROTECT:阻止上面的删除操作 但是弹出ProtectedError异常
SET_NULL 将外键字段设为null 只有当字段设置了null=True时 方可使用该值。
SET_DEFAULT:将外键字段设为默认值。只有当字段设置了default参数时 方可使用。
DO_NOTHING 什么也不做。
SET() 设置为一个传递给SET()的值或者一个回调函数的返回值。注意大小写。
'''
#SET() 的使用
def get_sentinel_user():
    return '''get_user_model().objects.get_or_create(username='deleted')[0]'''

class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )