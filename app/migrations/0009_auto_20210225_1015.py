# Generated by Django 3.1.7 on 2021-02-25 04:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20210225_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='serviceimage',
        ),
        migrations.RemoveField(
            model_name='referral',
            name='serviceimage',
        ),
        migrations.RemoveField(
            model_name='student',
            name='serviceimage',
        ),
    ]
