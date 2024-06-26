# Generated by Django 5.0.6 on 2024-06-07 16:48

import django.db.models.deletion
import product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_of_stock', models.BooleanField(default=False)),
                ('category', models.CharField(max_length=500)),
                ('quantity_in_stock', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=100)),
                ('size', models.CharField(max_length=500)),
                ('product_code', models.CharField(max_length=100, unique=True)),
                ('colors', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=product.models.get_image_upload_path)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='product.productitem')),
            ],
        ),
    ]
