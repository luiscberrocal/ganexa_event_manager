from django.test import TestCase

from .factories import EventFactory
from ..forms import TicketForm
from ..models import Ticket
from ...users.tests.factories import UserFactory


class TestTicketForm(TestCase):

    def test_is_valid(self):
        event = EventFactory.create(name='Spring Festival 2021')
        time_slots = event.create_times_slots(event.start_date, 1, 8, 100)
        data = {'first_name': 'John', 'last_name': 'Wick'}
        data['event'] = event
        data['owner'] = UserFactory.create()
        data['time_slot'] = time_slots[0]

        form = TicketForm(data=data)

        self.assertTrue(form.is_valid())
        form.save()
        data['owner'].refresh_from_db()
        # self.assertEqual(data['owner'].first_name, 'John')

        ticket = Ticket.objects.first()

        self.assertEqual(ticket.owner, data['owner'])
