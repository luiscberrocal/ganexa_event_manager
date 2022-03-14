from datetime import datetime

from django.core.management import BaseCommand

from ganexa_event_manager.events.models import Event


class Command(BaseCommand):
    """
        $ python manage.py time_slots --event-id=1 -d 2022-03-14 -t 08:00 --duration=1 -slot-count=8 -m 100
    """

    def add_arguments(self, parser):
        # parser.add_argument('requirement_filename')
        # parser.add_argument("-l", "--list",
        #                     action='store_true',
        #                     dest="list",
        #                     help="List data",
        #                     )

        parser.add_argument('-e', "--event-id",
                            dest="event_id",
                            help="Event to create the time slots for",
                            type=int
                            )

        parser.add_argument('-d', "--date",
                            dest="date",
                            help="Date to start slots",
                            )
        parser.add_argument('-t', "--time",
                            dest="time",
                            help="Time to start time slots",
                            )
        parser.add_argument('-du', "--duration",
                            dest="duration",
                            help="Duration of time slots in hours",
                            type=int
                            )
        parser.add_argument('-sc', "--slot-count",
                            dest="slot_count",
                            help="Number of slots for the day",
                            type=int
                            )
        parser.add_argument('-m', "--max-tickets",
                            dest="max_tickets",
                            help="Maximum number of tickets fot the time slot",
                            type=int
                            )

    def handle(self, *args, **options):
        start_date_str = f'{options["date"]} {options["time"]}'
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d %H:%M')
        try:
            event = Event.objects.get(id=options["event_id"])
            self.stdout.write(f'Event {event.name}')
            time_slots = event.create_times_slots(start_time=start_date, duration=options["duration"],
                                                  slot_count=options["slot_count"], max_tickets=options["max_tickets"])
            for i, time_slot in enumerate(time_slots, 1):
                self.stdout.write(f'{i} Time slot {time_slot.start_time} - {time_slot.end_time}')
        except Event.DoesNotExist:
            self.stderr.write(f'No event found for event id {options["event_id"]}')
