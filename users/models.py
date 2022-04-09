from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class notifications(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    header = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateField(auto_now_add=True)
    link = models.URLField()