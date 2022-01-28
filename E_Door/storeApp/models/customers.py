import email
import imp
from django.db import models

#customer table model
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    mobile_no = models.CharField(max_length=10)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    #to save this model data in db
    def register(self):
        self.save()
    

    @staticmethod
    def get_customer_by_email(email):
        try:
            return Customer.objects.get(email=email)
        except:
            return False
        
    def isExists(self):
        if Customer.objects.filter(email=self.email):
            return True
        else:
            return False