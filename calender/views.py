from django.shortcuts import render

# Create your views here.

def calender(request):
    """A view to render index page"""
    return render(request, 'calender/calender.html')
