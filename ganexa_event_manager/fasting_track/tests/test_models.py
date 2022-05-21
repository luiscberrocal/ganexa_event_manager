from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from ganexa_event_manager.fasting_track.tests.factories import FastingSessionFactory


class TestFastingSession(TestCase):

    def test_current_duration(self):
        start_hours_ago = 4
        start_date = timezone.now() - timedelta(hours=start_hours_ago)
        session = FastingSessionFactory.create(start_date=start_date)
        current_duration = session.current_duration
        self.assertIsNotNone(current_duration)
