# Generated by Django 5.1.4 on 2025-01-25 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_product_image_alter_shop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit_type',
            field=models.CharField(choices=[('units', 'Unidades'), ('lbs', 'Libras'), ('paqs', 'Paquetes')], max_length=10),
        ),
    ]
