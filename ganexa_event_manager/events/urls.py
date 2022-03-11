from django.urls import path

from ganexa_event_manager.events.views import get_events, get_event_buttons

app_name = 'events'
urlpatterns = [
    #Patient CRUD urls
    path(r'events-for-user', get_events, name='events-for-user'),
    path(r'actions-for-event/<int:event_id>/', get_event_buttons, name='actions-for-event'),
]
