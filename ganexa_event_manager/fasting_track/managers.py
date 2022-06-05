from typing import TYPE_CHECKING

from django.db import models
from django.db.models import Avg, Max

if TYPE_CHECKING:
    from django.conf import settings

    User = settings.AUTH_USER_MODEL


class FastingSessionManager(models.Manager):

    def average_hours(self, user: 'User', days: int = -1) -> float:
        if days > 2:
            average_qs = self.filter(end_date__isnull=False, user=user)[:days]
        else:
            average_qs = self.filter(end_date__isnull=False, user=user)

        average = average_qs.aggregate(Avg('duration'))
        return average['duration__avg']

    def longest_fasting_session(self, user: 'User'):
        qs = self.filter(end_date__isnull=False, user=user)
        max_duration = qs.aggregate(Max('duration'))
        fasting_sessions = qs.filter(duration=max_duration['duration__max'])
        return fasting_sessions.first()

