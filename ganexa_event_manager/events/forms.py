from django import forms
from django.db import transaction

from ganexa_event_manager.events.models import Ticket


class TicketForm(forms.ModelForm):
    # first_name = forms.CharField(max_length=80, label=_('Fist name'))
    # last_name = forms.CharField(max_length=80, label=_('Last name'))

    class Meta:
        model = Ticket
        fields = (
            # 'first_name',
            # 'last_name',
            'event',
            'owner',
            'time_slot',
        )

    def __init__(self, *args, **kwargs):
        current_event = kwargs.pop('event')
        current_owner = kwargs.pop('owner')
        super(TicketForm, self).__init__(*args, **kwargs)
        self.fields['event'].initial = current_event
        self.fields['owner'].initial = current_owner
        self.fields['event'].widget = forms.HiddenInput()
        self.fields['owner'].widget = forms.HiddenInput()

    def save(self, commit=True):
        # first_name = self.cleaned_data.pop('first_name')
        # last_name = self.cleaned_data.pop('last_name')
        if commit:
            # self.cleaned_data['owner'].first_name = first_name
            # self.cleaned_data['owner'].last_name = last_name
            with transaction.atomic():
                ticket = super(TicketForm, self).save(commit=commit)
                # self.cleaned_data['owner'].save()
                return ticket
