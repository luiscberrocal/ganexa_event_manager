from django.urls import path

from ganexa_event_manager.golf.views import range_hits_view

app_name = "golf"
urlpatterns = [
    path("range_hits/", view=range_hits_view, name="range-hits"),
]
