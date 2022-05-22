from django.urls import path

from .views import fasting_session_list_view, fasting_session_create_view, \
    fasting_session_update_view, fasting_session_delete_view, fasting_session_detail_view, fasting_session_main_view, \
    finish_fast

app_name = "fasting_track"
urlpatterns = [
    # FastingSession CRUD urls
    path(r'fasting-session/main/', fasting_session_main_view, name='main-fasting-session'),
    path(r'fasting-session/list/', fasting_session_list_view, name='list-fasting-session'),
    path(r'fasting-session/create/', fasting_session_create_view, name='create-fasting-session'),
    path(r'fasting-session/update/<int:pk>/', fasting_session_update_view, name='update-fasting-session'),
    path(r'fasting-session/delete/<int:pk>/', fasting_session_delete_view, name='delete-fasting-session'),
    path(r'fasting-session/<int:pk>/', fasting_session_detail_view, name='detail-fasting-session'),

    path('fasting-session/finish/<int:pk>/', finish_fast, name='finish-fasting-session')
]
