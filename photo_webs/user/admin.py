from django.contrib import admin
from .models import Profile, Follower, InstagramProfile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(InstagramProfile)
