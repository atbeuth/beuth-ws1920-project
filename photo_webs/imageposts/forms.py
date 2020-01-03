from django import forms
from .models import Imagepost

class ImagepostForm(forms.ModelForm):
    
    class Meta:
        model = Imagepost
        fields = ['title', 'img', 'description','long_description','freeuse','pinned','category','tags']

