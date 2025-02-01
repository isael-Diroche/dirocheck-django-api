from rest_framework import serializers
from .models import Product

# Create your serializers here.

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
    