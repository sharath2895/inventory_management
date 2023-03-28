from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class RegisterUser(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    def __str__(self):
        return self.first_name+''+self.last_name

    REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'email'
