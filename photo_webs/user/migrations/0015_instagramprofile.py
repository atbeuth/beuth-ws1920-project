# Generated by Django 2.2.6 on 2020-01-24 17:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0014_remove_profile_follow'),
    ]

    operations = [
        migrations.CreateModel(
            name='InstagramProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram_username', models.TextField(blank=True, max_length=100)),
                ('instagram_profile_img_url', models.TextField(blank=True, max_length=100)),
                ('instagram_posts', models.TextField(blank=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]