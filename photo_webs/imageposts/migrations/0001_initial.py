# Generated by Django 2.2.6 on 2019-10-21 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imagepost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=15)),
                ('img', models.ImageField(null=True, upload_to='')),
                ('description', models.TextField(max_length=1000)),
                ('tags', models.TextField(max_length=200)),
                ('username', models.TextField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('favs', models.IntegerField()),
            ],
        ),
    ]
