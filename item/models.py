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
    quantity = models.SmallIntegerField()
    sold = models.SmallIntegerField()
    available = models.SmallIntegerField()
    defective = models.SmallIntegerField()
    created_by = models.SmallIntegerField()
    updated_by = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
