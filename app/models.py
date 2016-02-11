from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

# Create your models here.
class signup(models.Model):
    userid=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    score=models.IntegerField(default=0)
    timestamp= models.DateTimeField(auto_now_add=True)
    array=models.CharField(max_length=800)
    def __str__(self):
        return  self.username

class questions(models.Model):
    question=models.CharField(max_length=500)
    op1=models.CharField(max_length=1000)
    op2=models.CharField(max_length=1000)
    op3=models.CharField(max_length=1000)
    op4=models.CharField(max_length=1000)
    ans=models.CharField(max_length=5)

    def __str__(self):
        return self.question
