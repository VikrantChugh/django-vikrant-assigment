from django.db import models
class Student(models.Model):
    stu_id=models.IntegerField()
    stu_name=models.CharField(max_length=20)
    stu_branch=models.CharField(max_length=10,default="cse")

    def __str__(self):
        return self.stu_name
      
      
# Create your models here.
