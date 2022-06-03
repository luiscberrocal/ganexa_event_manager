import datetime
from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from ganexa_event_manager.fasting_track.models import FastingSession
from ganexa_event_manager.fasting_track.tests.factories import FastingSessionFactory


class TestFastingSession(TestCase):

    def test_current_duration(self):
        start_hours_ago = 4
        start_date = timezone.now() - timedelta(hours=start_hours_ago)
        session = FastingSessionFactory.create(start_date=start_date)
        current_duration = session.current_duration
        self.assertIsNotNone(current_duration)

    def test_average(self):
        start_date = datetime.datetime(2022, 1, 1, 18, 0, 0)
        duration = timedelta(hours=18)
        end_date = start_date + duration
        session = FastingSessionFactory.create(start_date=start_date, end_date=end_date)

        start_date = datetime.datetime(2022, 1, 2, 15, 0, 0)
        duration = timedelta(hours=12)
        end_date = start_date + duration
        FastingSessionFactory.create(start_date=start_date, end_date=end_date, user=session.user)

        average = FastingSession.objects.average_hours(user=session.user)
        self.assertEqual(average, 15.0)
