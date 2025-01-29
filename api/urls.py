from django.urls import path, include
from rest_framework import routers
from api import views

# Registrar los ViewSets en el router
router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet, basename='product')
router.register(r'inventory', views.InventoryViewSet, basename='inventory')
router.register(r'shop', views.ShopViewSet, basename='shop')

# Configuración de las rutas
urlpatterns = [
    path('', include(router.urls)),  # Prefijo general ya será añadido desde `dirocheck/urls.py`
]
