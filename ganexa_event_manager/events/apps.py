from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = "ganexa_event_manager.events"
    verbose_name = _("Events")
