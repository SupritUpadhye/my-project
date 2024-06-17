# Generated by Django 5.0.6 on 2024-05-29 16:53

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_alter_productdetails_unit_parameter'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('Kg', 'kg'), ('Nos', 'Nos'), ('Dozen', 'Dozen'), ('gram', 'gram'), ('liter', 'liter'), ('ml', 'ml')], default='Kg', max_length=30),
        ),
    ]
