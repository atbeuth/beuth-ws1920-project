# Generated by Django 2.2.6 on 2019-10-31 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageposts', '0003_auto_20191021_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagepost',
            name='img',
            field=models.ImageField(default='media/773433.jpg', null=True, upload_to='media'),
        ),
    ]