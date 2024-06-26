# Generated by Django 5.0.6 on 2024-06-01 20:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_alter_productdetails_unit_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('Dozen', 'Dozen'), ('ml', 'ml'), ('Kg', 'kg'), ('Nos', 'Nos'), ('liter', 'liter'), ('gram', 'gram')], default='Kg', max_length=30),
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='products.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.products')),
            ],
        ),
    ]
