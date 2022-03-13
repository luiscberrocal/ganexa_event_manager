from django.test import TestCase

from .factories import EventFactory


class TestTicketForm(TestCase):

    def test_is_valid(self):
        event = EventFactory.create(name='Spring Festival 2021')
