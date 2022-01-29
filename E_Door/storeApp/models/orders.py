import imp
from operator import mod
from statistics import mode
from django.db import models
from numpy import product
from .products import Products
from .customers import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.FloatField()
    address=models.CharField(max_length=60,default='',blank=True)
    mobile_no = models.CharField(max_length=10)
    date = models.DateField(default=datetime.datetime.today)

    #to save the order details in the db 
    def placeOrder(self):
        self.save()
    
    @staticmethod
    def get_orders_by_customer(customer_id):
        return Orders.objects.filter(customer=customer_id).order_by('-date')
        