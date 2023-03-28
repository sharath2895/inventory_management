from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=30, null= True, default='')
    display_name = models.CharField(max_length=30, null= True,default='')


class User(models.Model):       
    role = models.ForeignKey(Role, on_delete=models.CASCADE,default=2)    
    mobile = models.CharField(max_length=10, null=True)     
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    intro = models.TextField(max_length=100, null=True)
    profile = models.TextField(max_length=200, null=True)    
                      
    def __str__(self):
        return self.first_name