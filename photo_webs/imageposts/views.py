from django.shortcuts import render, redirect
from django.views.generic import ListView 
from .models import Imagepost
from .forms import ImagepostForm

class ImagepostListView(ListView):
    model = Imagepost
    context_object_name = "all_imgposts"
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super(ImagepostListView, self).get_context_data(**kwargs) 
        context['imgposts_list'] = Imagepost.objects.all() 
        return context

def add_post(request):
    if request.method == 'POST':
        form = ImagepostForm(request.POST, request.FILES)
        if form.is_valid():
            imagepost=form.save()
            imagepost.user=request.user
            imagepost.save()
            return redirect('/') 
    else:
        form = ImagepostForm()
    return render(request, 'imageposts/post.html', {'form': form})