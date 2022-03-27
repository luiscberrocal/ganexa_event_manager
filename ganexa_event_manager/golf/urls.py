from django.urls import path

from .views import range_hits_view, save_hit_view

app_name = "golf"
urlpatterns = [
    path("range-hits/", view=range_hits_view, name="range-hits"),
    path("save-hit/", view=save_hit_view, name="save-hit"),
]
