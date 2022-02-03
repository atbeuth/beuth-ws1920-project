# Generated by Django 2.2.6 on 2019-11-01 12:21

import django_fields.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0003_auto_20191031_1247"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_banner",
            field=django_fields.fields.DefaultStaticImageField(
                default=0, upload_to="profile_imgs"
            ),
            preserve_default=False,
        ),
    ]
