from django.shortcuts import render, get_object_or_404
from .models import Performer
from .forms import PerformerForm

# Create your views here.
def magician(request):
    """A view to render magician for hire page"""

    adverts = Performer.objects.all()


    context = {
                 'adverts': adverts,
              }

    for advert in adverts:
        if advert.Display == False:
            pass
        else:
            return render(request, 'magician/magic_hire.html', context)    


def edit_advert(request):
    """ Display the user's order history and address. """
    advert = get_object_or_404(Performer, user=request.user)

    if request.method == 'POST':
        form = PerformerForm(request.POST, instance=advert)
        if form.is_valid():
            form.save()
            messages.success(request, 'Advert updated successfully')

    form = PerformerForm(instance=advert)

    template = 'magician/edit_hire.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
