import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from ganexa_event_manager.events.forms import TicketForm
from ganexa_event_manager.events.models import Event, Ticket

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
    try:
        event = Event.objects.get(id=event_id)
    except Event.DoesNotExist:
        event = None

    tickets = Ticket.objects.filter(owner=request.user, event__id=event_id)
    context = dict()
    context['event'] = event
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


@login_required
def ticket_form_view(request, event_id):
    if request.method == 'GET':
        template_name = 'events/partials/ticket_form.html'
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            event = None
        form = TicketForm(event=event, owner=request.user)
        context = {'form': form, 'event': event}
        response = render(request, template_name, context)
        return response
    if request.method == 'POST':
        form = TicketForm(data=request.POST)
        if form.is_valid():
            form.save()
            ticket = form.instance
            response = get_event_buttons(request, ticket.event.id)
            return response
        else:
            return HttpResponse('Error')
