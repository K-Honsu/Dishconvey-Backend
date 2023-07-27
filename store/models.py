from django.db import models
from django.conf import settings

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return f'{self.user} is a customer now'

class Collection(models.Model):
    title = models.CharField(max_length=200) 
    
    def __str__(self) -> str:
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    collection = models.ForeignKey(Collection, on_delete=models.PROTECT, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return self.title
  
    
