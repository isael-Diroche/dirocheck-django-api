from django.db import models
from module.shop.models import Shop

# Create your models here.

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    details = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True, default='none')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    unit_type = models.CharField(
        max_length=10,
        choices=[
            ('units', 'Unidades'), 
            ('lbs', 'Libras'), 
            ('paqs', 'Paquetes')
        ]
    )
    # expiration_date = models.DateField(blank=True, null=True)
    # image = models.ImageField(upload_to='product_images/', blank=True, null=True, default='/default.png')
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.details

    def save(self, *args, **kwargs):
        self.price = float(self.price)
        self.stock = int(self.stock)
        self.total = self.price * self.stock
        super().save(*args, **kwargs)
        
class Category(models.Model): 
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='categories')
    name = models.CharField(max_length=30)
    color = models.CharField(
        max_length=10,
        choices=[
            ('#ffe3e7', 'Pink'), 
            ('#d5e4ff', 'Blue'), 
            ('#ccffc4', 'Green'), 
            ('#eeff86', 'Yellow'), 
            ('#ffdddd', 'Red')
        ],
        verbose_name="Color de etiqueta"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Última Actualización")
    
    class Meta:
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"
        ordering = ['name']
    
    def __str__(self):
        return self.name
