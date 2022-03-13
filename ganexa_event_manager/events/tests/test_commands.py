import datetime

from django.core.management import call_command
from django.test import TestCase

from .factories import EventFactory
from ..models import TimeSlot


class TestTimeSlotsCommand(TestCase):

    def test_create_time_slots(self):
        event_duration_days = 2
        duration_per_day_hours = 9  # hours
        slots_duratition_hours = 1
        start_date = datetime.datetime(2021, 3, 1, 7, 15, 0)
        end_date = start_date + datetime.timedelta(days=event_duration_days) + \
                   datetime.timedelta(hours=duration_per_day_hours)
        event = EventFactory.create(start_date=start_date, end_date=end_date)
        call_command('time_slots', event_id=event.id, date='2021-03-01',
                     time='07:15', duration=1, slot_count=9, max_tickets=110)
        self.assertEqual(TimeSlot.objects.count(), 9)
        first_time_slot = TimeSlot.objects.first()
        last_time_slot = TimeSlot.objects.last()
        self.assertEqual(first_time_slot.end_time,
                         datetime.datetime(2021, 3, 1, 8, 15, 0).replace(tzinfo=datetime.timezone.utc))
        self.assertEqual(last_time_slot.end_time,
                         datetime.datetime(2021, 3, 1, 16, 15, 0).replace(tzinfo=datetime.timezone.utc))
