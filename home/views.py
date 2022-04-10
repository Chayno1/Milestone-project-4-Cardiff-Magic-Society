from django.shortcuts import render

# Create your views here.


def index(request):
    """A view to render index page"""
    return render(request, 'home/index.html')


def maintenance(request):
    """A view to render maintenance page"""
    return render(request, 'home/maintenance.html')    


def join(request):
    """A view to render how to join page"""
    return render(request, 'home/join.html')  