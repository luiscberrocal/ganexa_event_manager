from crispy_forms.helper import FormHelper
from django import forms
from django.utils import timezone
from django.utils.timezone import localtime

from .models import FastingSession


class FastingSessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(FastingSessionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'fasting-form'
#        self.helper.add_input(Submit('submit', _('Save')))
        date_format = "%Y-%m-%dT%H:%M"
        local_now = localtime(timezone.now())
        self.fields['start_date'].initial = local_now.strftime(date_format)
        self.fields['start_date'].widget = forms.DateTimeInput(format=date_format,
                                                               attrs={'type': 'datetime-local'})
        self.fields['user'].initial = self.user
        self.fields['user'].widget = forms.HiddenInput()
        if self.instance.end_date is not None:
            self.fields['end_date'].widget = forms.DateTimeInput(format=date_format,
                                                                 attrs={'type': 'datetime-local'})
        else:
            self.fields['end_date'].widget = forms.HiddenInput()

    class Meta:
        model = FastingSession
        fields = (
            'start_date',
            'end_date',
            'target_duration',
            'comments',
            'user',
        )
        widgets = {
           # 'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


