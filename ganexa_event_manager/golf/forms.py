from django import forms

from ganexa_event_manager.golf.models import RangeHit


class RangeHitForm(forms.ModelForm):
    class Meta:
        model = RangeHit
        fields = (
            'course',
            'player',
            'club',
            'distance',
            'direction',
            'hit_classification',
        )
