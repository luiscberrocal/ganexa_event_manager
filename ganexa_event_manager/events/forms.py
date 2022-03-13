from django import forms
from django.utils.translation import ugettext_lazy as _

from ganexa_event_manager.events.models import Ticket


class TicketModel(forms.ModelForm):
    first_name = forms.CharField(max_length=80, label=_('Fist name'))
    last_name = forms.CharField(max_length=80, label=_('Last name'))

    class Meta:
        model = Ticket
        fields = (
            'first_name',
            'last_name',
            'event',
            'owner',
            'time_slot',
        )
