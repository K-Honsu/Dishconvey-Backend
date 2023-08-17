from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from .enums import PaymentStatus
import uuid

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return f'{self.user} is a customer'

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
    
    
class Cart(models.Model):
    id = models.UUIDField(unique=True, default=uuid.uuid4, primary_key=True)
    
    def __str__(self) -> str:
        return f'Cart ID is {self.id}'
    
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1)]
    )
    
    class Meta:
        unique_together = [['cart', 'product']]
        
    def __str__(self) -> str:
        return f'Cart belong to {self.cart.id}'
    
    
class Order(models.Model):
    # create model for orders
    placed_at = models.DateTimeField(auto_now_add=True)
    payment_status = models.CharField(choices=[(status.value, status.name) for status in PaymentStatus], default=PaymentStatus.PENDING)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f'{self.customer} has placed an order at {self.placed_at} time and payment status is ->{self.payment_status}'
    
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='orderitems')
    quantity = models.PositiveSmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    
    def __str__(self) -> str:
        return f'OrderItem is {self.product} -> {self.order}'
    
  
    
