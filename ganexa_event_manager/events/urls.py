from django.urls import path

from ganexa_event_manager.events.views import get_events

app_name = 'events'
urlpatterns = [
    #Patient CRUD urls
    path(r'events-for-user', get_events, name='events-for-user'),
]
