# Generated by Django 5.1.4 on 2024-12-30 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_shop_inventory_product_shop'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
