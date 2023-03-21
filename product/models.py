from django.db import models

# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=20, null= True)
    summary =  models.CharField(max_length=50, null= True)
    type = models.CharField(max_length=15, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
class ProductMeta(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    key = models.CharField(max_length=20, null= True)
    content = models.CharField(max_length=50, null= True)