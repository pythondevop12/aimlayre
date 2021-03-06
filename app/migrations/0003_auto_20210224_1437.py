# Generated by Django 3.1.7 on 2021-02-24 09:07

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210224_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='about',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='home',
            name='aboutimage',
            field=cloudinary.models.CloudinaryField(default='', max_length=255, verbose_name='image'),
            preserve_default=False,
        ),
    ]
