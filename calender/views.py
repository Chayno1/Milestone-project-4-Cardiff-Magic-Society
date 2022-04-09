from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Event, Member_status
from .forms import EventForm
# Create your views here.




def calender(request):
    """A view to render index page"""

    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'calender/calender.html', context)


@login_required    
def add_event(request):
    """ Add an event to calender """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only site admin can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Successfully added Event!')
            return redirect(reverse('calender'))
        else:
            messages.error(request, 'Failed to add event. Please ensure the form is valid.')
    else:
        form = EventForm()
        
    template = 'calender/add_event.html'
    context = {
        'form': form,
    }

    return render(request, template, context)