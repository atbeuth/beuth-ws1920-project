# Generated by Django 2.2.6 on 2019-10-31 12:40

from django.db import migrations
import django_fields.fields


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=django_fields.fields.DefaultStaticImageField(null=True, upload_to='profile_imgs'),
        ),
    ]
