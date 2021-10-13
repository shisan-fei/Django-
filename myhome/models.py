from django.db import models

# Create your models here.

#创建学生模型
class stu(models.Model):
    name = models.CharField(max_length=20)     #
    age = models.IntegerField(default=24)
    sex = models.CharField(max_length=1,default=0)
    address = models.CharField(max_length=50,null=True)
    
    # def __repr__(self):
    #     return f'<stu: stu object (id:{self.id},name:{self.name})>'    
        #返回<QuerySet [<stu: stu object (id:1,name:wlf)>, <stu: stu object (id:2,name:李四)>]>
    
#创建书籍模型    
class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    publish = models.CharField(max_length=100)  #出版社
    abstract = models.TextField()     #介绍
    img_url = models.CharField(max_length=150)   #封面
    pub_data = models.DateField()      #出版时间
    priice = models.FloatField()       #价格
         
