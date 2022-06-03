from typing import TYPE_CHECKING

from django.db import models
from django.db.models import Avg

if TYPE_CHECKING:
    from django.conf import settings

    User = settings.AUTH_USER_MODEL


class FastingSessionManager(models.Manager):

    def average_hours(self, user: 'User', days: int = 7) -> float:
        average_qs = self.filter(end_date__isnull=False, user=user)[:days]
        average = average_qs.aggregate(Avg('duration'))
        return average['duration__avg']
