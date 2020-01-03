from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    return render(request, 'web/home.html')

def license(request):
    return render(request, 'web/license.html')

def license_de(request):
    return render(request, 'web/license_de.html')