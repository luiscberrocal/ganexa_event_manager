from django.urls import path

from .views import get_events, get_event_buttons, ticket_form_view, delete_ticket_view, get_ticket_view

app_name = 'events'
urlpatterns = [
    # Patient CRUD urls
    path(r'events-for-user', get_events, name='events-for-user'),
    path(r'actions-for-event/<int:event_id>/', get_event_buttons, name='actions-for-event'),
    path(r'ticket/create/<int:event_id>/', ticket_form_view, name='ticket-create'),
    path(r'ticket/delete/<int:ticket_id>/', delete_ticket_view, name='ticket-delete'),
    path(r'ticket/<int:ticket_id>/', get_ticket_view, name='ticket-details'),
]
