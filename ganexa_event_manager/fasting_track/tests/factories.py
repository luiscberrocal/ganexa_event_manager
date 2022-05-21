from django.conf import settings
from factory import LazyAttribute
from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Factory as FakerFactory
from pytz import timezone

from ganexa_event_manager.fasting_track.models import FastingSession
from ganexa_event_manager.users.tests.factories import UserFactory

faker = FakerFactory.create()


class FastingSessionFactory(DjangoModelFactory):
    class Meta:
        model = FastingSession

    # id = BigAutoField We do not support this field type
    user = SubFactory(UserFactory)
    start_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                                 tzinfo=timezone(settings.TIME_ZONE)))
    # end_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
    #                                                           tzinfo=timezone(settings.TIME_ZONE)))
    end_date = None
    duration = 16
    # duration = PositiveSmallIntegerField We do not support this field type
    # target_duration = PositiveSmallIntegerField We do not support this field type
    comments = LazyAttribute(lambda x: faker.text(max_nb_chars=180))
