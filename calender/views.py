from django.shortcuts import render, get_object_or_404
from .models import Event, Member_status

# Create your views here.




def calender(request):
    """A view to render index page"""

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'calender/calender.html', context)
