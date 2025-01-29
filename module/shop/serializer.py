from rest_framework import serializers
from .models import Shop

# Create your serializers here.
class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'
