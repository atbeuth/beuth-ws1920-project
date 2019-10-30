from django.shortcuts import render
from django.views.generic import ListView 
from .models import Imagepost

#Image view Page
class ImagepostListView(ListView):
    model = Imagepost
    context_object_name = "all_imgposts"
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super(ImagepostListView, self).get_context_data(**kwargs) 
        context['imgposts_list'] = Imagepost.objects.all() 
        return context
