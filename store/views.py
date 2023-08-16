from .models import *
from .serializers import *
from .permissions import IsAdminOrReadOnly
from django.db.models.aggregates import Count
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import RetrieveModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin, ListModelMixin
from rest_framework.response import Response

class CustomerViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    """_summary_
    This endpoint allows administrators to create, retrieve, and update customer profiles.
    Admins can create new customer profiles, while users can access and modify their own profiles.
    Admin access required for customer profile creation.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAdminUser]
    
    @action(detail=False, methods=['GET','PUT'], permission_classes=[IsAuthenticated])
    def me(self, request):
        """
        Retrieve or update the profile of the currently authenticated user.
        """
        customer = Customer.objects.get(user_id=request.user.id)
        if request.method == 'GET':
            serializer = CustomerSerializer(customer)
            return Response(serializer.data)
        elif request.method == 'PUT':
            serializer = CustomerSerializer(customer, data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
            
            

class ProductViewSet(ModelViewSet):
    """_summary_

    This endpoint facilitates viewing, creation, updating, and deletion of products.
    Users can view product details, and admins can perform write operations (create, update, delete).
    Admin access required for write operations.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    
class CollectionViewSet(ModelViewSet):
    """_summary_
    This endpoint allows management of collections containing products.
    View, create, update, and delete product collections.
    Provides product count within each collection.
    Admin access required for write operations.
    """
    queryset = Collection.objects.annotate(product_count=Count('products')).all()
    serializer_class = CollectionSerializer
    permission_classes = [IsAdminOrReadOnly]
    
# cart views
class CartViewSet(CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, ListModelMixin,GenericViewSet):
    """_summary_
    Manage shopping carts for users.
    Create, retrieve, and delete shopping carts.
    Access cart items and associated products.
    Optimized performance with prefetching related items and products.
    Supports cart creation, retrieval, and deletion.
    """
    queryset = Cart.objects.prefetch_related('items__product').all()
    serializer_class = CartSerializers
    
class CartItemViewSet(ModelViewSet):
    """_summary_
    This endpoint facilitates managing items within a user's cart.
    Get, add, update, and remove cart items.
    Supports multiple HTTP methods (GET, POST, PATCH, DELETE).
    Provides context for cart item serializer.
    Admin access required for update and delete operations.
    """
    http_method_names = ['get', 'post', 'patch', 'delete']
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
    
    def get_serializer_class(self):
        if self.request.method == 'POST':
            return AddCartItemSerializer
        elif self.request.method == 'PATCH':
            return UpdateCartItemSerializer
        return CartItemSerializer
    
    def get_serializer_context(self):
        return {'cart_id' : self.kwargs['cart_pk']}