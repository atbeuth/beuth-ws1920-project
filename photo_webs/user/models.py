from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_fields import DefaultStaticImageField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = DefaultStaticImageField(upload_to='profile_imgs', default_image_path='profile_imgs/default_profile_img.jpeg')
    profile_banner = DefaultStaticImageField(upload_to='profile_imgs', default_image_path='profile_imgs/default_profile_banner.jpeg')
    bio_short = models.TextField(max_length=100, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    show_location = models.BooleanField(default=True) 
    show_email = models.BooleanField(default=False)
    birth_date = models.DateField(null=True, blank=True)

    # for badges
    is_verified = models.BooleanField(default=False) 
    is_pro = models.BooleanField(default=False)

    follow = models.ManyToManyField('self', related_name='follows', symmetrical=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)