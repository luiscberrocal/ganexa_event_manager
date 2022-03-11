from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel


class Event(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=100)
    start_date = models.DateField(_('Start date'))
    end_date = models.DateField(_('End date'))
    max_tickets_per_day = models.PositiveSmallIntegerField(_('Max tickets per day'))

    def __str__(self):
        return self.name


class TimeSlot(TimeStampedModel):
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='time_slots', on_delete=models.CASCADE)
    start_time = models.DateTimeField(_('Start time'))
    end_time = models.DateTimeField(_('End time'))
    max_tickets = models.IntegerField(_('Max tickets'))

    def __str__(self):
        return f'{self.event.name} {self.start_time}-{self.end_time}'

    class Meta:
        ordering = ('start_time',)


class Ticket(TimeStampedModel):
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='tickets', on_delete=models.PROTECT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Owner'), related_name='tickets',
                              on_delete=models.PROTECT)
    time_slot = models.ForeignKey(TimeSlot, verbose_name=_('Time slot'), related_name='tickets',
                                  on_delete=models.PROTECT)

    #def __str__(self):
    #    return _(f'Ticket for {self.owner} for {self.time_slot.start_time}')
