from django import forms
from .models import Imagepost

class ImagepostForm(forms.ModelForm):
    
    class Meta:
        model = Imagepost
        fields = ['title', 'img', 'description','long_description','license_text','pinned','category','tags']

        widgets = {
            "license_text": forms.Textarea(attrs={"placeholder": "Enter nothing for PhotoHub license or select free to use. Text entered here is used as license text."})
        }
