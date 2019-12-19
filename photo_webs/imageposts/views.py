from django.shortcuts import render, redirect
from django.views.generic import ListView 
from .models import Imagepost
from .forms import ImagepostForm

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys


class ImagepostListView(ListView):
    model = Imagepost
    context_object_name = "all_imgposts"
    template_name = 'web/home.html'

    def get_context_data(self, **kwargs):
        context = super(ImagepostListView, self).get_context_data(**kwargs) 
        context['imgposts_list'] = Imagepost.objects.all() 
        return context

def create_thumbnail(imageFile, imageName):
    im = Image.open(imageFile)

     # resize image
    max_size = (1600, 900)
    im.thumbnail(max_size, Image.ANTIALIAS)

    # crop image
    im_height = im.size[1]
    im_width = im.size[0]
    im_ratio = im_height / float(im_width)

    new_ratio = 16 / 9

    left = 0
    right = im_width
    top = 0
    bottom = im_height

    if not im_ratio == new_ratio:
        if im_height < im_width:
            new_width = (im_height / 9) * 16

            left = (im_width - new_width) / 2
            right = left + new_width
            top = 0
            bottom = im_height
        else:
            new_height = (im_width / 16 ) * 9

            left = 0
            right = im_width
            top = (im_height - new_height ) / 2
            bottom = top + new_height

    cropped_im = im.crop((left, top, right, bottom))

    # save image to object
    im_io = BytesIO()
    cropped_im.save(im_io, format='JPEG')
    im_io.seek(0)

    # build and  InMemoryUploadedFile from im
    im_file = InMemoryUploadedFile(im_io, None, imageName, 'image/jpeg', sys.getsizeof(im_io), None)
    return im_file


def add_post(request):
    if request.method == 'POST':
        form = ImagepostForm(request.POST, request.FILES)
        if form.is_valid():
            imagepost=form.save()
            imagepost.user=request.user

            imagepost.img_thumbnail = create_thumbnail(form.cleaned_data['img'], imagepost.img.name)

            imagepost.save()
            return redirect('/') 
    else:
        form = ImagepostForm()
    return render(request, 'imageposts/post.html', {'form': form})