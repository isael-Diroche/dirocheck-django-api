from django.db import models

# Create your models here.

from django.db import models

class Product(models.Model):
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
