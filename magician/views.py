from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Performer
from .forms import PerformerForm

# Create your views here.

def magician(request):
    """A view to render magician for hire page"""

    adverts = Performer.objects.all()

    context = {
                 'adverts': adverts,
              }

    return render(request, 'magician/magic_hire.html', context)    


@login_required    
def add_hire(request):
    """ Add an advert to magicians for hire """

    if request.method == 'POST':
        form = PerformerForm(request.POST, request.FILES)
        if form.is_valid():
            advert = form.save()
            messages.success(request, 'Successfully added advert!')
            return redirect(reverse('magician'))
        else:
            messages.error(request, 'Failed to add advert. Please ensure the form is valid.')
    else:
        form = PerformerForm()
        
    template = 'magician/add_hire.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required 
def edit_advert(request, advert_id):
    """ Edit an advert on magicians for hire """

    advert = get_object_or_404(Performer, pk=advert_id)
    if request.method == 'POST':
        form = PerformerForm(request.POST, request.FILES, instance=advert)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated advert!')
            return redirect(reverse('magician'))
        else:
            messages.error(request, 'Failed to update advert. Please ensure the form is valid.')
    else:
        form = PerformerForm(instance=advert)
        messages.info(request, f'You are editing {advert.name}')

    template = 'magician/edit_hire.html'
    context = {
        'form': form,
        'advert': advert,
        
    }

    return render(request, template, context)
