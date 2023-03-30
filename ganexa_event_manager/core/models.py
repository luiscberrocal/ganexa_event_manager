from django.conf import settings
from django.db import models
from django.utils import timezone
from model_utils.models import TimeStampedModel
from django.utils.translation import gettext_lazy as _


class AuditableModel(models.Model):
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="created_%(class)s", null=True, on_delete=models.SET_NULL
    )
    modified_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="modified_%(class)s", null=True, on_delete=models.SET_NULL
    )

    class Meta:
        abstract = True


class TimedTask(AuditableModel, TimeStampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('User'),
                              related_name='owned_%(class)s',
                              on_delete=models.CASCADE)
    start_date = models.DateTimeField(_('Start date'))
    end_date = models.DateTimeField(_('End date'), null=True, blank=True)
    duration = models.DurationField(_('Duration'), null=True, blank=True)
    comments = models.CharField(_('Comments'), max_length=180, null=True, blank=True)
    is_negative = models.BooleanField(_('Is negative'), default=False)

    class Meta:
        ordering = ('-start_date',)
        abstract = True

    @property
    def elapsed(self) -> float:
        if self.end_date is None:
            end_date = timezone.now()
        else:
            end_date = self.end_date
        if self.is_negative:
            elapsed_duration = self.start_date - end_date
        else:
            elapsed_duration = end_date - self.start_date

        return elapsed_duration

    def __str__(self):
        return f'{self.owner.username} {self.start_date} {self.duration}'

    def finish(self, commit: bool = True) -> float:
        self.end_date = timezone.now()
        self.duration = self.elapsed
        if commit:
            self.save()
        return self.duration

    def save(self, *args, **kwargs):
        self.duration = self.elapsed
        super(TimedTask, self).save(*args, **kwargs)
