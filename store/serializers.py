from .models import *
from rest_framework import serializers

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'phone_number','date_of_birth', 'address']



class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'title', 'description', 'price', 'collection']
        
class CollectionSerializer(serializers.ModelSerializer):
    product_count = serializers.IntegerField()
    
    class Meta:
        model = Collection
        fields = ['id', 'title', 'product_count']
        
# cart serializers
class CartSerializers(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    class Meta:
        model = Cart
        fields = ['id']