from django.urls import path, include
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'product', views.ProductViewSet)
router.register(r'inventory', views.InventoryViewSet)
router.register(r'shop', views.ShopViewSet, basename='shop')

urlpatterns = [
    path('', include(router.urls)),
]
