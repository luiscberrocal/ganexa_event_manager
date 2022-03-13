import datetime

from django.test import TestCase

from ganexa_event_manager.events.models import TimeSlot
from ganexa_event_manager.events.tests.factories import EventFactory


class TestEvent(TestCase):

    def test_create_time_slots(self):
        duration = 2
        duration_hours = 9  # hours
        start_date = datetime.datetime(2021, 3, 1, 7, 15, 0)
        end_date = start_date + datetime.timedelta(days=duration) + datetime.timedelta(hours=duration_hours)
        event = EventFactory.create(start_date=start_date, end_date=end_date)
        time_slots = event.create_times_slots(start_date, 1, 9, 110)
        self.assertEqual(TimeSlot.objects.count(), 9)
        self.assertEqual(time_slots[0].end_time, datetime.datetime(2021, 3, 1, 8, 15, 0))
        self.assertEqual(time_slots[8].end_time, datetime.datetime(2021, 3, 1, 16, 15, 0))
