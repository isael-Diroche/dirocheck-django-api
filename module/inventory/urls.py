from django.urls import path, include
from rest_framework import routers
from .views import InventoryViewSet

# Registrar los ViewSets en el router
router = routers.DefaultRouter()
router.register(r'inventory', InventoryViewSet, basename='inventory')

# Configuración de las rutas
urlpatterns = [
    path('', include(router.urls)),  # Prefijo general ya será añadido desde `dirocheck/urls.py`
]
