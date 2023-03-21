from django.db import models
from product.models import Product
from item.models import Item
from order.models import Order

# Create your models here.
class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete= models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    store_keeping_unit = models.CharField(max_length=20, null= True)
    price = models.DecimalField(max_digits=4, decimal_places=4, null=True)
    discount = models.DecimalField(max_digits=4, decimal_places=4, null= True)
    quantity = models.SmallIntegerField(null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    context = models.TextField(max_length=100, null=True)

    