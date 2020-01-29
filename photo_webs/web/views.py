from django.shortcuts import render
from django.shortcuts import render_to_response

from imageposts.models import Imagepost
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, 'web/home.html')

def license(request):
    return render(request, 'web/license.html')

def license_de(request):
    return render(request, 'web/license_de.html')

def imprint(request):
    return render(request, 'web/terms.html')

def imprint_de(request):
    return render(request, 'web/terms_de.html')
def search(request, pk):
    return render(request, 'web/search.html', {'pk':   pk, 'all_users': User.objects.all(),'all_imgposts': reversed(Imagepost.objects.all())})
