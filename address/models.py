from django.db import models
from user.models import User
# from order.models import Order

# Create your models here.


class Address(models.Model):
    # order = models.ForeignKey(Order, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, null= True)
    line_1 = models.CharField(max_length=200, null=True)
    line_2 = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    pin_code = models.CharField(max_length=10, null=True)
    land_mark = models.CharField(max_length=100, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.type
