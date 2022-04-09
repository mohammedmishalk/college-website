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
          user = models.ForeignKey(User,on_delete=models.CASCADE)
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
