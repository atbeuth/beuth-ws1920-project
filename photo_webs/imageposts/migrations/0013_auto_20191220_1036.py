# Generated by Django 2.2.6 on 2019-12-20 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageposts', '0012_auto_20191219_0826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagepost',
            name='freeuse',
        ),
        migrations.AddField(
            model_name='imagepost',
            name='license_text',
            field=models.TextField(null=True),
        ),
    ]