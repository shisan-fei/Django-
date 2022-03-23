from django.db import models
import os


#使用__str__来返回一个字符串
class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birth_date = models.DateField()

    def __str__(self):
        return self.first_name + self.last_name

#upload_to参数用于设置上传地址，可以接收一个回调函数，该函数返回具体的路径字符串
#定义一个函数，返回一个文件目录
def get_photo(self, filename):
    return os.path.join('photo',
                        '%s_%s%s' % (self.class_name,
                                    self.name,
                                    os.path.splitext(filename)[1]))
#ImageField字段传入照片
class pic(models.Model):
    picture=models.ImageField(upload_to=get_photo, height_field=None, width_field=None, max_length=100, **options)  #upload_to 指定get_photo函数返回的地址，存入照片。
    # 文件被传至`MEDIA_ROOT/uploads`目录，MEDIA_ROOT由你在settings文件中设置。真实路径为/media/uploads
    upload = models.FileField(upload_to='uploads/')
    # 或者 被传到`MEDIA_ROOT/uploads/2015/01/30`目录，增加了一个时间划分
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')



