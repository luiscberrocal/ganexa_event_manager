from django.urls import path

from .views import get_events, get_event_buttons, ticket_form_view

app_name = 'events'
urlpatterns = [
    # Patient CRUD urls
    path(r'events-for-user', get_events, name='events-for-user'),
    path(r'actions-for-event/<int:event_id>/', get_event_buttons, name='actions-for-event'),
    path(r'ticket/create/<int:event_id>/', ticket_form_view, name='ticket-create'),
]
