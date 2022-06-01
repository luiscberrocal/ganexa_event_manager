from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django import forms
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .models import FastingSession


class FastingSessionForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super(FastingSessionForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_id = 'fasting-form'
        self.helper.add_input(Submit('submit', _('Save')))
        date_format = "%Y-%m-%dT%H:%M"
        self.fields['start_date'].initial = timezone.now().strftime(date_format)
        self.fields['start_date'].widget = forms.DateTimeInput(format=date_format,
                                                               attrs={'type': 'datetime-local'})
        self.fields['user'].initial = self.user
        self.fields['user'].widget = forms.HiddenInput()

    class Meta:
        model = FastingSession
        fields = (
            'start_date',
            'target_duration',
            'comments',
            'user',
        )
        widgets = {
           # 'start_date': forms.DateTimeInput(attrs={'type': 'datetime-local'})
        }


