from datetime import timedelta
from random import randint

from django.conf import settings
from factory import LazyAttribute
from factory import SubFactory
from factory import lazy_attribute
from factory.django import DjangoModelFactory
from faker import Factory as FakerFactory
from pytz import timezone

from ..models import Event, TimeSlot, Ticket
from ...users.tests.factories import UserFactory

faker = FakerFactory.create()


class EventFactory(DjangoModelFactory):
    class Meta:
        model = Event

    name = LazyAttribute(lambda x: faker.text(max_nb_chars=100))
    start_date = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                                 tzinfo=timezone(settings.TIME_ZONE)))
    max_tickets_per_day = LazyAttribute(lambda o: randint(1, 100))

    @lazy_attribute
    def end_date(self):
        days = randint(1, 7)
        return self.start_date + timedelta(days=days)


class TimeSlotFactory(DjangoModelFactory):
    class Meta:
        model = TimeSlot

    event = SubFactory(EventFactory)
    start_time = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                                 tzinfo=timezone(settings.TIME_ZONE)))
    end_time = LazyAttribute(lambda x: faker.date_time_between(start_date="-1y", end_date="now",
                                                               tzinfo=timezone(settings.TIME_ZONE)))
    max_tickets = LazyAttribute(lambda o: randint(1, 100))


class TicketFactory(DjangoModelFactory):
    class Meta:
        model = Ticket

    event = SubFactory(EventFactory)
    owner = SubFactory(UserFactory)
    time_slot = SubFactory(TimeSlotFactory)
