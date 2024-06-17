# Generated by Django 5.0.6 on 2024-05-24 21:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_alter_productdetails_unit_parameter'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerPage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bannerImg', models.ImageField(blank=True, default='products/fruitica.png', null=True, upload_to='products/images')),
                ('mainTitle', models.CharField(max_length=50)),
                ('subTitle', models.CharField(max_length=70)),
                ('short_desc', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='productdetails',
            name='unit_parameter',
            field=models.CharField(choices=[('Nos', 'Nos'), ('ml', 'ml'), ('Kg', 'kg'), ('liter', 'liter'), ('Dozen', 'Dozen')], default='Kg', max_length=30),
        ),
        migrations.AddField(
            model_name='productdetails',
            name='baner_page',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='product_details', to='products.bannerpage'),
        ),
        migrations.AddField(
            model_name='products',
            name='baner_page',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.bannerpage'),
        ),
    ]
