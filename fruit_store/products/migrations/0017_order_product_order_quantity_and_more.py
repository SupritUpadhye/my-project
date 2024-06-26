# Generated by Django 5.0.6 on 2024-05-31 17:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_alter_productdetails_unit_parameter_checkoutaddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, related_name='product_order', to='products.products'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('liter', 'liter'), ('Kg', 'kg'), ('Nos', 'Nos'), ('gram', 'gram'), ('ml', 'ml'), ('Dozen', 'Dozen')], default='Kg', max_length=30),
        ),
    ]
