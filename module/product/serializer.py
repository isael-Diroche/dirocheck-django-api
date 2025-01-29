from rest_framework import serializers
from .models import Product

# Create your serializers here.

class ProductSerializer(serializers.ModelSerializer):
    # image_url = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
    
    # def get_image_url(self, obj):
    #     request = self.context.get('request')
    #     if obj.image and request:
    #         return request.build_absolute_uri(obj.image.url)
    #     return None