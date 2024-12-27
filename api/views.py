from django.shortcuts import render
from rest_framework import viewsets
from .serializer import ProductsSerializer
from .models import Products

# Create your views here.

class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer