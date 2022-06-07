from datetime import datetime, timedelta
from typing import List

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
from model_utils.models import TimeStampedModel


class Event(TimeStampedModel):
    name = models.CharField(_('Name'), max_length=100)
    start_date = models.DateField(_('Start date'))
    end_date = models.DateField(_('End date'))
    max_tickets_per_day = models.PositiveSmallIntegerField(_('Max tickets per day'))

    def __str__(self):
        return self.name

    def create_times_slots(self, start_time: datetime, duration: int, slot_count: int,
                           max_tickets: int) -> List['TimeSlot']:
        time_slots = []
        current_time = start_time
        for _ in range(slot_count):
            time_slot = TimeSlot(event=self, start_time=current_time,
                                 end_time=current_time + timedelta(hours=duration),
                                 max_tickets=max_tickets)
            time_slots.append(time_slot)
            current_time += timedelta(hours=duration)
        return TimeSlot.objects.bulk_create(time_slots)


class TimeSlot(TimeStampedModel):
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='time_slots', on_delete=models.CASCADE)
    start_time = models.DateTimeField(_('Start time'))
    end_time = models.DateTimeField(_('End time'))
    max_tickets = models.IntegerField(_('Max tickets'))

    def __str__(self):
        date = self.start_time.strftime('%d-%b-%y')
        start_time = self.start_time.strftime('%H:%M')
        end_time = self.end_time.strftime('%H:%M')
        return f'{date} {start_time}-{end_time}'

    class Meta:
        ordering = ('start_time',)


class Ticket(TimeStampedModel):
    event = models.ForeignKey(Event, verbose_name=_('Event'), related_name='tickets', on_delete=models.PROTECT)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_('Owner'), related_name='tickets',
                              on_delete=models.PROTECT)
    time_slot = models.ForeignKey(TimeSlot, verbose_name=_('Time slot'), related_name='tickets',
                                  on_delete=models.PROTECT)

    # def __str__(self):
    #    return _(f'Ticket for {self.owner} for {self.time_slot.start_time}')
