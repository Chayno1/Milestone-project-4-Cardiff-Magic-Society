from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Gallery
from .forms import GalleryForm

# Create your views here.
def all_images(request):
    """ A view to show all images """
    images = Gallery.objects.all()

    context = {
        'images': images,
    }

    return render(request, 'gallery/gallery.html', context)


@login_required    
def add_image(request):
    """ Add a image to gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = GalleryForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added image!')
            return redirect(reverse('gallery'))
        else:
            messages.error(request, 'Failed to add image. Please ensure the form is valid.')
    else:
        form = GalleryForm()
        
    template = 'gallery/add_image.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
