from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True, default='shop_images/image_default.webp')
    contact_number = models.CharField(max_length=17, blank=True, null=True)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='products')
    details = models.TextField(blank=True)
    category = models.CharField(max_length=50, blank=True, default='none')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    unit_type = models.CharField(
        max_length=10,
        choices=[('units', 'Unidades'), ('lbs', 'Libras')]
    )
    expiration_date = models.DateField(blank=True, null=True)
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.details

    def save(self, *args, **kwargs):
        self.total = self.price * self.stock
        super().save(*args, **kwargs)

class Inventory(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='inventories')
    products = models.ManyToManyField(Product, related_name='inventories', blank=True)  # `blank=True` para permitir vacío
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
