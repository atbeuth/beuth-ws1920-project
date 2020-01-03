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

def image_resize_and_autorotate(imageFile, imageName):
    im = Image.open(imageFile)
    file_format = im.format
    exif = im._getexif()

    im.thumbnail((4096, 4096), resample=Image.ANTIALIAS)

    # if image has exif data about orientation, let's rotate it
    orientation_key = 274 # cf ExifTags
    if exif and orientation_key in exif:
        orientation = exif[orientation_key]

        rotate_values = {
            3: Image.ROTATE_180,
            6: Image.ROTATE_270,
            8: Image.ROTATE_90
        }

        if orientation in rotate_values:
            im = im.transpose(rotate_values[orientation])

    im_io = BytesIO()
    im.save(im_io, format='JPEG')
    im_io.seek(0)

    im_file = InMemoryUploadedFile(im_io, None, imageName, 'image/jpeg', sys.getsizeof(im_io), None)
    return im_file

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

            imagepost.img = image_resize_and_autorotate(form.cleaned_data['img'], imagepost.img.name)
            imagepost.img_thumbnail = create_thumbnail(form.cleaned_data['img'], imagepost.img.name)
          
            imagepost.save()
            return redirect('/') 
    else:
        form = ImagepostForm()
    return render(request, 'imageposts/post.html', {'form': form})