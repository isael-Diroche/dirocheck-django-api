from django.db import models

# Create your models here.

class Shop(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='shop_images/', blank=True, null=True, default='/default.png')
    contact_number = models.CharField(max_length=17, blank=True, null=True)
    type = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name