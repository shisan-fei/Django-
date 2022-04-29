from statistics import mode
from tabnanny import verbose
from time import perf_counter
from typing import Tuple
from unicodedata import name
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(verbose_name='姓名',max_length=20,primary_key=True)
    password = models.CharField(verbose_name='密码',max_length=20)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        db_table='user'
        verbose_name= verbose_name_plural = '用户表'


    