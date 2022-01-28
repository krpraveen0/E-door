import imp
from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models
from .categories import Category

class Products(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(default=0.00)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/products/')



    @staticmethod
    def get_product_by_id(ids):
        return Products.objects.get(id__in=ids)
    
    @staticmethod
    def get_all_products():
        return Products.objects.all()
    
    @staticmethod
    def get_all_products_by_category_id(category_id):
        if category_id:
            return Products.objects.filter(category=category_id)
        else:
            return Products.get_all_products()