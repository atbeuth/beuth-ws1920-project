from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_fields import DefaultStaticImageField

class Profile_Manager(models.Manager):
    def toggle_follow(self, user, request_user, username_to_toggle):
        profile = Profile.objects.get(user__username__iexact=username_to_toggle)
        if request_user in profile.followers.all():
            profile.followers.remove(request_user)
            request_user.profile.following.remove(user)
        else:
            profile.followers.add(request_user)
            request_user.profile.following.add(user)
        return profile

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

    following = models.ManyToManyField(User, related_name='following', blank=True) # These users I am following
    followers = models.ManyToManyField(User, related_name='is_following', blank=True) # These users are following me

    objects = Profile_Manager()

    # for badges
    is_verified = models.BooleanField(default=False) 
    is_pro = models.BooleanField(default=False)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()


class Follower(models.Model):
    follower = models.ForeignKey(User, related_name='followinga', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followersa', on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ('follower', 'following')

    def __unicode__(self):
        return u'%s follows %s' % (self.follower, self.following)

class Post(models.Model):
    title = models.TextField()
    cover = models.ImageField(upload_to='media')

    def __str__(self):
        return self.title