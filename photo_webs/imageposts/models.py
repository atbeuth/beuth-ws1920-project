from django.db import models

from django.contrib.auth.models import User

CATEGORY_CHOICES = (
    ('no category','NO CATEGORY'),
    ('nature','NATURE'),
    ('humans', 'HUMANS'),
    ('animals','ANIMALS'),
    ('buildings','BUILDINGS'),
    ('abstract','ABSTRACT'),
    ('wallpaper','WALLPAPER'),
)


class Imagepost(models.Model):
    title = models.TextField(max_length=15) 
    img = models.ImageField(upload_to='media', null=True, default='media/773433.jpg')
    img_thumbnail = models.ImageField(upload_to='media/thumbnails', null=True, default='media/773433.jpg')
    description = models.TextField(max_length=100)
    long_description = models.TextField(max_length=1000)
    license_text = models.TextField(null=True)
    pinned = models.BooleanField(default=False) 
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='green')
    tags = models.TextField(null=True, max_length=200)
    username = models.TextField(max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(auto_now=True) 
    favs = models.IntegerField(default=0)

    def summary(self):
        return self.title + ': ' + self.description
    def __str__(self):
        return self.title + ' +' + str(self.favs)