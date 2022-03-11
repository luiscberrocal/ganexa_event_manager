from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from ganexa_event_manager.events.models import Event


@login_required
def get_events(request):
    template_name = 'events/partials/events_for_user.html'
    events = Event.objects.all()
    context = {'events': events}
    response = render(request, template_name, context)
    return response
