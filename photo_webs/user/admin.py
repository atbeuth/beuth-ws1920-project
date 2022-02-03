from django.contrib import admin

from .models import Follower, InstagramProfile, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Follower)
admin.site.register(InstagramProfile)
