# Generated by Django 5.0.1 on 2024-02-01 09:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_productprice_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coffeeproducts',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='names', to='products.coffeecategory'),
        ),
    ]
