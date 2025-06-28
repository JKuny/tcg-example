import datetime
import os
import random

from django.core.management.base import BaseCommand
from django.utils import timezone
from lorem import get_paragraph

from events.models import Event

# python manage.py seed --mode=refresh

""" Clear all data and creates events """
MODE_REFRESH = "refresh"

""" Clear all data and do not create any object """
MODE_CLEAR = "clear"


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")


def clear_data():
    """Deletes all the table data"""
    Event.objects.all().delete()


def create_event():
    """Creates an event object combining different elements from the list"""
    games = ["Magic: The Gathering", "Flesh & Blood", "Lorcana", "Pokemon", "Yu-Gi-Oh"]
    game_format = ["Casual", "Tournament", "Draft", "Pre-release"]
    price = [0, 10, 15, 35]
    player_spaces = [8, 16]

    event = Event(
        game_name=random.choice(games),
        start_date=timezone.now().date(),
        start_time=timezone.now().time(),
        end_time=(timezone.now() + datetime.timedelta(hours=2)).time(),
        player_spaces=random.choice(player_spaces),
        description=get_paragraph(
            count=1,
            comma=(0, 2),
            word_range=(4, 8),
            sentence_range=(5, 10),
            sep=os.linesep,
        ),
        rules=random.choice(game_format),
        price=random.choice(price),
    )

    event.save()
    return event


def run_seed(self, mode):
    """Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    # Creating 15 events
    for i in range(15):
        create_event()
