from django.db import models

class Imagepost(models.Model):
    title = models.TextField(max_length=15) 
    img = models.ImageField(upload_to='media', null=True)
    description = models.TextField(max_length=1000)
    tags = models.TextField(max_length=200)
    username = models.TextField(max_length=50) 
    timestamp = models.DateTimeField(auto_now=True) 
    favs = models.IntegerField()

    def summary(self):
        return self.title + ': ' + self.description
    def __str__(self):
        return self.title + ' +' + str(self.favs)