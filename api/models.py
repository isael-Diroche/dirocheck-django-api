from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
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
    products = models.ManyToManyField(Product, related_name='inventories')
    name = models.CharField(max_length=100)  # Name of the inventory, e.g., month
    total = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
        
    def __str__(self):
        return f"{self.name} - {self.shop.name}"
        
    def save(self, *args, **kwargs):
        self.total = sum(product.total for product in self.products.all())
        super().save(*args, **kwargs)