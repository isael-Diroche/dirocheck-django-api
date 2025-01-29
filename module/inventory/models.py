from django.db import models
from module.product.models import Product
from module.shop.models import Shop

# Create your models here.

class Inventory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='inventories')
    products = models.ManyToManyField(Product, related_name='inventories', blank=True)
    name = models.CharField(max_length=100)  # Name of the inventory, e.g., month
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"{self.name} - {self.shop.name}"

    def save(self, *args, **kwargs):
        # Guardar el objeto primero si aún no tiene un ID asignado
        if not self.pk:  # Si la instancia aún no tiene ID
            super().save(*args, **kwargs)
        
        # Si hay productos, calcula el total; de lo contrario, establece total en 0
        self.total = sum(product.total for product in self.products.all()) if self.products.exists() else 0
        
        # Guarda nuevamente con el total actualizado
        super().save(update_fields=['total'])
