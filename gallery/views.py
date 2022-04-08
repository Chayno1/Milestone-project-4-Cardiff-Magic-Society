from django.shortcuts import render
from .models import Gallery

# Create your views here.
def all_images(request):
    """ A view to show all images """
    images = Gallery.objects.all()

    context = {
        'images': images,
    }

    return render(request, 'gallery/gallery.html', context)