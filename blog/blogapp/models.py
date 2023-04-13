from django.db import models
from datetime import datetime

from django.forms import forms


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='profile')
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.title

class Comments(models.Model):
    title=models.CharField(max_length=100,null=True,blank=True)
    comments = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(auto_now_add=True, blank=True)

class Reply_comment(models.Model):
    comments = models.CharField(max_length=100,null=True,blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)

# Add any additional methods or properties as needed
class CustomerDetails(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True,unique=True)
    email=models.EmailField(max_length=100, null=True, blank=True,unique=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    confirmpassword=models.CharField(max_length=100, null=True, blank=True)

