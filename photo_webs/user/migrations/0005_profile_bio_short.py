# Generated by Django 2.2.6 on 2019-11-01 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0004_profile_profile_banner"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="bio_short",
            field=models.TextField(blank=True, max_length=20),
        ),
    ]
