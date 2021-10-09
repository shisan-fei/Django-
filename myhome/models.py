from django.db import models

# Create your models here.

class stu(models.Model):
    name = models.CharField(max_length=20)     #
    age = models.IntegerField(default=24)
    sex = models.CharField(max_length=1,default=0)
    address = models.CharField(max_length=50,null=True)
