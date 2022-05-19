from django.conf import settings
from django.db import models

# Create your models here.
from django.utils import timezone
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _
from ganexa_event_manager.core.models import AuditableModel


class FastingSession(AuditableModel, TimeStampedModel):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'), related_name='fasting_sessions',
                             on_delete=models.PROTECT)
    start_date = models.DateTimeField(_('Start date'))
    end_date = models.DateTimeField(_('End date'), null=True, blank=True)
    comments = models.CharField(_('Comments'), max_length=180, null=True, blank=True)

    @property
    def duration(self):
        if self.end_date is None:
            end_date = timezone.now()
        else:
            end_date = self.end_date
        return end_date - self.start_date

    class Meta:
        ordering = ('start_date',)

    def __str__(self):
        return f'{self.user.username} {self.start_date} {self.duration}'

