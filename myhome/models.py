from django.db import models

# Create your models here.

class stu(models.Model):
    name = models.CharField(max_length=20)     #
    age = models.IntegerField(default=24)
    sex = models.CharField(max_length=1,default=0)
    address = models.CharField(max_length=50,null=True)
    
    def __repr__(self):
        return f'<stu: stu object (id:{self.id},name:{self.name})>'    
        #返回<QuerySet [<stu: stu object (id:1,name:wlf)>, <stu: stu object (id:2,name:李四)>]>
