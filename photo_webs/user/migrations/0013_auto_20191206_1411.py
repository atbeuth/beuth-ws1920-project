# Generated by Django 2.2.6 on 2019-12-06 13:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0012_merge_20191206_1352'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='is_following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follower',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followinga', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='follower',
            name='following',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='followersa', to=settings.AUTH_USER_MODEL),
        ),
    ]
