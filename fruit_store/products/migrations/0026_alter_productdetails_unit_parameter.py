# Generated by Django 5.0.6 on 2024-06-02 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_cart_product_alter_productdetails_unit_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('liter', 'liter'), ('Dozen', 'Dozen'), ('ml', 'ml'), ('gram', 'gram'), ('Kg', 'kg'), ('Nos', 'Nos')], default='Kg', max_length=30),
        ),
    ]
