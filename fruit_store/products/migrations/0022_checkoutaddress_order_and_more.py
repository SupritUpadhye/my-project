# Generated by Django 5.0.6 on 2024-06-02 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0021_alter_productdetails_unit_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkoutaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='checkout_addresses', to='products.order'),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('liter', 'liter'), ('Nos', 'Nos'), ('Kg', 'kg'), ('ml', 'ml'), ('Dozen', 'Dozen'), ('gram', 'gram')], default='Kg', max_length=30),
        ),
    ]