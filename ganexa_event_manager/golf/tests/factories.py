import string

from django.conf import settings
from factory import Iterator
from factory import LazyAttribute
from factory import SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyText
from faker import Factory as FakerFactory

from ganexa_event_manager.golf.models import GolfCourse, GolfClub, HitClassification, RangeHit
from ganexa_event_manager.users.tests.factories import UserFactory

faker = FakerFactory.create()


class GolfCourseFactory(DjangoModelFactory):
    class Meta:
        model = GolfCourse

    # id = BigAutoField We do not support this field type
    name = LazyAttribute(lambda x: faker.text(max_nb_chars=80))
    short_name = LazyAttribute(lambda x: faker.text(max_nb_chars=30))
    country = LazyAttribute(lambda x: FuzzyText(length=3, chars=string.ascii_letters).fuzz())


class GolfClubFactory(DjangoModelFactory):
    class Meta:
        model = GolfClub

    player = SubFactory(UserFactory)
    name = Iterator(settings.STANDARD_GOLF_GLUBS)
    order = 1
    # order = PositiveSmallIntegerField We do not support this field type


class HitClassificationFactory(DjangoModelFactory):
    class Meta:
        model = HitClassification

    # id = BigAutoField We do not support this field type
    # order = PositiveSmallIntegerField We do not support this field type
    order = 1
    player = SubFactory(UserFactory)
    name = LazyAttribute(lambda x: faker.text(max_nb_chars=30))
    hit_type = 1
    # hit_type = PositiveSmallIntegerField We do not support this field type


class RangeHitFactory(DjangoModelFactory):
    class Meta:
        model = RangeHit

    # id = BigAutoField We do not support this field type
    course = SubFactory(GolfCourseFactory)
    player = SubFactory(UserFactory)
    club = SubFactory(GolfClubFactory)
    distance = Iterator([50, 100, 200, 250, 300])
    direction = Iterator(RangeHit.DIRECTION_CHOICES, getter=lambda x: x[0])
    hit_classification = SubFactory(HitClassificationFactory)
