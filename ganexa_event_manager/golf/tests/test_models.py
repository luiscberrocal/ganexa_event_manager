from django.db.models import Avg, Count
from django.test import TestCase

from ganexa_event_manager.golf.models import GolfClub
from ganexa_event_manager.golf.tests.factories import GolfCourseFactory, RangeHitFactory
from ganexa_event_manager.users.tests.factories import UserFactory


class TestRangeHit(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.player = UserFactory.create()
        GolfClub.objects.create_golf_clubs(cls.player)
        cls.course = GolfCourseFactory.create()


    def test_average(self):
        hits = RangeHitFactory.create_batch(5, player=self.player, course=self.course,
                                            club=self.player.golf_clubs.first())
        golf_clubs = GolfClub.objects.filter(player=self.player).annotate(average_distance=Avg('range_hits__distance'))
        self.assertEqual(len(hits), 5)
