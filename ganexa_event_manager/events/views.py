from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from ganexa_event_manager.events.models import Event, Ticket

import logging

logger = logging.getLogger(__name__)
@login_required
def get_events(request):
    template_name = 'events/partials/events_for_user.html'
    events = Event.objects.all()
    context = {'events': events}
    response = render(request, template_name, context)
    return response

@login_required
def get_event_buttons(request, event_id):
    template_name = 'events/partials/event_buttons.html'
    tickets = Ticket.objects.filter(owner=request.user, event__id=event_id)
    context = dict()
    if tickets.count() == 0:
        context['ticket'] = None
    elif tickets.count() == 1:
        context['ticket'] = tickets.first()
    else:
        msg = f'User {request.user} has more than one ticket'
        logger.warning(msg)
        context['ticket'] = None
        context['error'] = msg
    response = render(request, template_name, context)
    return response
