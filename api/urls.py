from django.urls import path, include
from rest_framework import routers

from module.inventory.views import InventoryViewSet
from module.shop.views import ShopViewSet
from module.product.views import ProductViewSet, CategoryViewSet
# Registrar los ViewSets en el router
router = routers.DefaultRouter()
router.register(r'product', ProductViewSet, basename='product')
router.register(r'inventory', InventoryViewSet, basename='inventory')
router.register(r'shop', ShopViewSet, basename='shop')
router.register(r'category', CategoryViewSet, basename='category')


# Configuración de las rutas
urlpatterns = [
    path('', include(router.urls)),
]
