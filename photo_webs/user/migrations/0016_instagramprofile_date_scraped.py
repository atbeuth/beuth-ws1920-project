# Generated by Django 2.2.6 on 2020-01-26 19:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0015_instagramprofile"),
    ]

    operations = [
        migrations.AddField(
            model_name="instagramprofile",
            name="date_scraped",
            field=models.TextField(blank=True),
        ),
    ]
