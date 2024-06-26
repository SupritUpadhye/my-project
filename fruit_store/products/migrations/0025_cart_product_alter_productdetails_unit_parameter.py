# Generated by Django 5.0.6 on 2024-06-02 15:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_alter_productdetails_unit_parameter'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='products.products'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('gram', 'gram'), ('Kg', 'kg'), ('ml', 'ml'), ('Dozen', 'Dozen'), ('liter', 'liter'), ('Nos', 'Nos')], default='Kg', max_length=30),
        ),
    ]
