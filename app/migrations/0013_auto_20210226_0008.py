# Generated by Django 3.1.7 on 2021-02-25 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20210225_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='message',
            field=models.TextField(),
        ),
    ]
