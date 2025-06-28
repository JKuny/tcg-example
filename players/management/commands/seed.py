import random

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import models

from players.models import Player

# Use via:
#   python manage.py seed --mode=refresh

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
    Player.objects.all().delete()


def create_player():
    """Creates a user object combining different elements from the list"""
    preferred_game_options = ["Magic: The Gathering", "Flesh & Blood",
                              "Lorcana", "Pokemon", "Yu-Gi-Oh"]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    player = Player(
        user,
        preferred_game=random.choice(preferred_game_options)
    )

    player.save()
    return player


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
        create_player()
