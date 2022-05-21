from django.urls import path

from .views import range_hits_view, save_hit_view, list_player_hits_view, delete_range_hit, golf_club_stats_view

app_name = "golf"
urlpatterns = [
    path("range-hits/", view=range_hits_view, name="range-hits"),
    path("save-hit/", view=save_hit_view, name="save-hit"),
    path("player-hits/", view=list_player_hits_view, name="player-hits"),
    path("player-hit/delete/<int:pk>/", view=delete_range_hit, name="player-hit-delete"),
    path("golf-club/<int:pk>/", view=golf_club_stats_view, name="golf-club-stats"),
]
