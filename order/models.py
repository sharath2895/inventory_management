from django.db import models
from user.models import User
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=10, null=True)
    status = models.CharField(max_length=20, null=True)
    sub_total = models.IntegerField(null=True)
    item_discount = models.DecimalField(max_digits=4, max_length=10, null=True,decimal_places=4)
    tax = models.DecimalField(max_digits=4, max_length=10, null=True,decimal_places=4)
    shipping = models.DecimalField(max_digits=4, max_length=10, null=True,decimal_places=4)
    order_total = models.DecimalField(max_digits=4, max_length=10, null=True,decimal_places=4)
    promo = models.CharField(max_length=30, null=True)
    discount = models.DecimalField(max_digits=4, max_length=10, null=True,decimal_places=4)
    grand_total = models.DecimalField(max_digits=4, max_length=10, null=True,decimal_places=4)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
