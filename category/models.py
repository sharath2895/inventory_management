from django.db import models
from product.models import Product

# Create your models here.


class Category(models.Model):
    parent = models.CharField(max_length=20, null=True)
    title = models.CharField(max_length= 20, null=True)
    meta_title = models.CharField(max_length=20, null=True)
    slug = models.SlugField(default='', null=True)
    content = models.TextField(max_length=50, null=True)
    
    
class ProductCatergory(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)