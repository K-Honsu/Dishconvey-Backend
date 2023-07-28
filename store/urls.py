from . import views
from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register('products', views.ProductViewSet)
router.register('collections', views.CollectionViewSet)
router.register('customer', views.CustomerViewSet)
router.register('carts', views.CartViewSet)

urlpatterns = router.urls