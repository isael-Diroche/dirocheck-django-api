from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .serializer import ProductSerializer, InventorySerializer, ShopSerializer
from .models import Product, Inventory, Shop

# Create your views here.
    
class ShopViewSet(ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    
@api_view(['DELETE'])
def delete_shop(request, pk):
    shop = get_object_or_404(Shop, pk=pk)
    shop.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer