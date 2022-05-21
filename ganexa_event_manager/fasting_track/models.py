from django.conf import settings
from django.db import models
# Create your models here.
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

from ganexa_event_manager.core.models import AuditableModel


class FastingSession(AuditableModel, TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='fasting_sessions',
                             on_delete=models.PROTECT)
    start_date = models.DateTimeField(_('Start date'))
    end_date = models.DateTimeField(_('End date'), null=True, blank=True)
    duration = models.PositiveSmallIntegerField(_('Duration'), default=0)
    target_duration = models.PositiveSmallIntegerField(_('Target duration'), default=16)
    comments = models.CharField(_('Comments'), max_length=180, null=True, blank=True)

    @property
    def current_duration(self) -> float:
        if self.end_date is None:
            end_date = timezone.now()
        else:
            end_date = self.end_date
        elapsed = end_date - self.start_date
        return elapsed.seconds / 3600

    @property
    def completed(self) -> float:
        return self.current_duration / self.target_duration

    class Meta:
        ordering = ('start_date',)

    def __str__(self):
        return f'{self.user.username} {self.start_date} {self.duration}'
