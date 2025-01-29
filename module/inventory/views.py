from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializer import InventorySerializer
from .models import Inventory

# Create your views here.

class InventoryViewSet(ModelViewSet):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer