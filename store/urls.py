from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('customer', views.CustomerViewSet)
router.register('carts', views.CartViewSet)
router.register('orders', views.OrderViewSet)

cart_router = routers.NestedDefaultRouter(router, 'carts', lookup='cart')
cart_router.register('items', views.CartItemViewSet, basename='cart-items')


urlpatterns = router.urls + cart_router.urls 