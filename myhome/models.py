from django.db import models

# Create your models here.

#创建学生模型
class stu(models.Model):
    name = models.CharField(primary_key=True,max_length=20)     #字符串类型，定义为主键
    age = models.IntegerField(default=24)  #整型  int
    sex = models.CharField(max_length=1,default=0)
    address = models.CharField(max_length=50,null=True)   #null=True 可以为空
    
    # def __repr__(self):
    #     return f'<stu: stu object (id:{self.id},name:{self.name})>'    
        #返回<QuerySet [<stu: stu object (id:1,name:wlf)>, <stu: stu object (id:2,name:李四)>]>

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'students'
        verbose_name = verbose_name_plural = '学生信息'
    
#创建书籍模型    
class Book(models.Model):
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=50)
    publish = models.CharField(max_length=100)  #出版社
    abstract = models.TextField()     #介绍
    img_url = models.CharField(max_length=150)   #封面
    pub_data = models.DateField()      #出版时间
    priice = models.FloatField()       #价格

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'book'
        verbose_name = verbose_name_plural = '书籍信息'
         
