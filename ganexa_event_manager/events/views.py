import logging

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .forms import TicketForm
from .models import Event, Ticket

logger = logging.getLogger(__name__)


# @login_required
def get_events(request):
    template_name = 'events/partials/events_for_user.html'
    events = Event.objects.all()
    context = {'events': events}
    response = render(request, template_name, context)
    return response


@login_required
def get_event_actions(request, event_id):
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
            response = get_event_actions(request, ticket.event.id)
            return response
        else:
            return HttpResponse('Error')


@login_required
def delete_ticket_view(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
    except Ticket.DoesNotExist:
        logger.error(f'Not ticket for id {ticket_id}')
    if ticket.owner == request.user:
        event = ticket.event
        ticket.delete()
        response = get_event_actions(request, event.id)
        return response
    else:
        logger.error('You cannot delete a ticket that you do not own')


@login_required
def get_ticket_view(request, ticket_id):
    try:
        ticket = Ticket.objects.get(id=ticket_id)
        template_name = 'events/partials/ticket_detail.html'
        context = {'ticket': ticket}
        response = render(request, template_name, context)
        return response
    except Ticket.DoesNotExist:
        logger.error(f'No ticket for {ticket_id}')
