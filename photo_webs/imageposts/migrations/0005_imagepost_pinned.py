# Generated by Django 2.2.6 on 2019-11-02 00:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageposts', '0004_auto_20191031_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagepost',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
