# Generated by Django 5.0.6 on 2024-06-05 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_user_logintime'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='logintime',
        ),
    ]
