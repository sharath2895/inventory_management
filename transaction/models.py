from django.db import models
from user.models import User
from order.models import Order

# Create your models here.


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    code = models.CharField(max_length=15, null=True)
    type = models.CharField(max_length=10, default='', null=True)
    mode = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=10, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    context = models.CharField(max_length=10, null=True)
