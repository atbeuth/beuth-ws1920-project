from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Imagepost
from .forms import ImagepostForm

from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

from django.shortcuts import get_object_or_404

class ImageDetailView(DetailView):
    model = Imagepost
    context_object_name = 'image'

class ImagepostListView(ListView):
    model = Imagepost
    context_object_name = "all_imgposts"
    paginate_by = 24
    template_name = 'web/home.html'
    ordering = ["-timestamp"]

def image_resize_and_autorotate(imageFile, imageName):
    im = Image.open(imageFile)
    exif = im._getexif()

    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")

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

    if cropped_im.mode in ("RGBA", "P"):
        cropped_im = cropped_im.convert("RGB")

    # save image to object
    im_io = BytesIO()
    cropped_im.save(im_io, format='JPEG')
    im_io.seek(0)

    # build and  InMemoryUploadedFile from im
    im_file = InMemoryUploadedFile(im_io, None, imageName, 'image/jpeg', sys.getsizeof(im_io), None)
    return im_file

PHOTOHUB_LICENSE = """PhotoHub license - use of images
Images on PhotoHub are provided under the PhotoHub license under the following conditions.
The PhotoHub license gives you an irrevocable, worldwide, non-exclusive and royalty-free right to use, download, copy and modify the images for commercial and non-commercial purposes. It is not necessary to name the photo author or PhotoHub, but we would be happy to provide a voluntary source.

The PhotoHub license does not allow:

- the sale or distribution of images in digital and physical form, in particular as stock photos or digital wallpapers;

- the sale or distribution of images e.g. as posters, digital prints or physical products, without adding additional elements or otherwise creating added value;

- depicting identifiable people in an offensive, pornographic, obscene, immoral, defamatory or political manner;

- or the suggestion that depicted people, brands, organizations, etc. endorse certain products or services unless authorized to do so.

Please note that although all content on PhotoHub is freely usable for commercial and non-commercial purposes, elements shown in the images, such as identifiable people, logos and brands, may be subject to additional copyrights, property rights, personal rights, trademark rights, etc. Third party approval or licensing of these rights may be required, particularly for commercial applications. PhotoHub does not guarantee that such consent or licenses have been obtained and expressly disclaims any liability in this regard.
"""

def add_post(request):
    if request.method == 'POST':
        form = ImagepostForm(request.POST, request.FILES)
        if form.is_valid():
            imagepost=form.save()
            imagepost.user=request.user

            if not form.cleaned_data['license_text'] :
                imagepost.license_text = PHOTOHUB_LICENSE

            imagepost.img = image_resize_and_autorotate(form.cleaned_data['img'], imagepost.img.name)
            imagepost.img_thumbnail = create_thumbnail(form.cleaned_data['img'], imagepost.img.name)
          
            imagepost.save()
            return redirect('/') 
    else:
        form = ImagepostForm()
    return render(request, 'imageposts/post.html', {'form': form})


def edit_post(request, pk):
    post = get_object_or_404(Imagepost, pk=pk)
    if request.method == "POST":
        form = ImagepostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/imageposts/post/{}/edit/'.format(pk), pk=pk)
    else:
        if (request.user != post.user):
            return redirect('/imageposts/post/{}/'.format(pk), pk=pk)
        else:
            form = ImagepostForm(instance=post)
            return render(request, 'imageposts/edit_imagepost.html', {'form': form, 'pk': pk})