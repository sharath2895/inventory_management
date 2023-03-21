from django.db import models

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Role(models.Model):
    name = models.CharField(max_length=30, null= True, default='')
    display_name = models.CharField(max_length=30, null= True,default='')


class User(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, default='', null= True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    user_name = models.CharField(unique=True, null=False, max_length=30)
    mobile = models.CharField(max_length=10, null=True)
    email = models.EmailField(max_length=150, unique=True, null=False)
    password_hash = models.CharField(max_length=40, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    intro = models.TextField(max_length=100, null=True)
    profile = models.TextField(max_length=200, null=True)
    
      
    def __str__(self):
        return self.name 