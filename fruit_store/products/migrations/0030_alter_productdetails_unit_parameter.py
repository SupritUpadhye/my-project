# Generated by Django 5.0.6 on 2024-06-05 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0029_alter_productdetails_unit_parameter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('ml', 'ml'), ('Dozen', 'Dozen'), ('Kg', 'kg'), ('gram', 'gram'), ('Nos', 'Nos'), ('liter', 'liter')], default='Kg', max_length=30),
        ),
    ]
