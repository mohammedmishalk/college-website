from msilib.schema import Class
from django.db import models
from django.contrib.auth.models import User


class Students(models.Model):
          user = models.ForeignKey(User,on_delete=models.CASCADE)
          Department = models.CharField(max_length= 20,null=True)
          Phone_number = models.CharField(max_length=10)
          DoB =models.DateField(null=True)
          Photo =models.ImageField(null=True, blank=True, upload_to="images/",default="images/example3.jpg")
          Parent_name =models.CharField(max_length=30)
          Contact_number =models.CharField(max_length=10)

class Teachers(models.Model):
          user = models.ForeignKey(User,on_delete=models.CASCADE,db_constraint=False)
          Department = models.CharField(max_length= 20,null=True)
          Subject = models.CharField(max_length=30)
          Qualifications = models.CharField(max_length=100)
          Phone_number = models.CharField(max_length=10)
          Photo =models.ImageField(null=True, blank=True, upload_to="images/",default="images/example3.jpg")


class Staf(models.Model):
          user = models.ForeignKey(User,on_delete=models.CASCADE)
          Dutty = models.CharField(max_length= 20,null=True)
          Phone_number = models.CharField(max_length=10)
          Photo =models.ImageField(null=True, blank=True, upload_to="images/",default="images/example3.jpg")

class Gallery(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    Photo =models.ImageField(null=False, upload_to="gallery/")
    disc = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    accepted = models.BooleanField(default=False)

class Department(models.Model):
    name = models.CharField(max_length=50)
    course = models.CharField(max_length=100)
    HOD = models.ForeignKey(Teachers,on_delete=models.DO_NOTHING)    
    teachers = models.ManyToManyField(Teachers,related_name='teachers')
    course_fee = models.JSONField(default = list)

class TimeTable(models.Model):
    teacher = models.IntegerField()
    dprt = models.IntegerField()
    Class = models.IntegerField()
    day = models.JSONField(default = dict)

class Syllabus(models.Model):
    dprt = models.IntegerField()
    pdf =models.FileField(null=False, upload_to="pdf/")




