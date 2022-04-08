from django.shortcuts import render

# Create your views here.

def gallery(request):
    """A view to render gallery page"""
    return render(request, 'gallery/gallery.html')
