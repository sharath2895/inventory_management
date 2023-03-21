import datetime
from django.db import models
from product.models import Product
from order.models import Order

# Create your models here.


class Brand(models.Model):
    title = models.CharField(max_length=20, null=True)
    summary = models.CharField(max_length=20, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    context = models.CharField(max_length=30, null=False)


class Item(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    supplier = models.CharField(max_length=10, null=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_keeping_unit = models.CharField(max_length=20, null=True)
    mrp = models.DecimalField(max_digits=4, null=True, decimal_places=4)
    discount = models.DecimalField(max_digits=4, null=True, decimal_places=4)
    price = models.DecimalField(max_digits=4, null=True, decimal_places=4)
    quantity = models.SmallIntegerField(max_length=10)
    sold = models.SmallIntegerField(max_length=10)
    available = models.SmallIntegerField(max_length=10)
    defective = models.SmallIntegerField(max_length=10)
    created_by = models.SmallIntegerField(max_length=5)
    updated_by = models.SmallIntegerField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
