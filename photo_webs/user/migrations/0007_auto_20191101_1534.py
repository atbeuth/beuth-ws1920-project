# Generated by Django 2.2.6 on 2019-11-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20191101_1532'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio_short',
            field=models.TextField(blank=True, max_length=100),
        ),
    ]
