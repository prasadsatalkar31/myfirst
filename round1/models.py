from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Signup(models.Model):
	userid = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	score = models.IntegerField(default=0)
	timestamp = models.IntegerField(default=1800)
	array = models.CharField(max_length=800,default="1;2;3;4;5;6;7;8;9;10;11;12;13;14;15;16;17;18;19;20")

	def __str__(self):
		return self.userid

class Questions(models.Model):
    question=models.CharField(max_length=500)
    op1=models.CharField(max_length=1000)
    op2=models.CharField(max_length=1000)
    op3=models.CharField(max_length=1000)
    op4=models.CharField(max_length=1000)
    ans=models.CharField(max_length=5)

    def __str__(self):
        return self.question