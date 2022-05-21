from django import forms

from .models import FastingSession


class FastingSessionForm(forms.ModelForm):
    class Meta:
        model = FastingSession
        fields = (
            'start_date',
            'target_duration',
            'comments',
        )
