from django.shortcuts import render

# Create your views here.


def shop(request):
    """A view to render shop page"""
    return render(request, 'shop/shop.html')