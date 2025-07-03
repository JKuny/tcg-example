import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from players.models import Player

MODE_REFRESH = "refresh"
MODE_CLEAR = "clear"

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument("--mode", type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write("seeding player data...")
        run_seed(self, options["mode"])
        self.stdout.write("done.")

def clear_data():
    """Deletes all the table data"""
    Player.objects.all().delete()
    User.objects.all().delete()

def create_player():
    """Creates a user object combining different elements from the list"""
    preferred_game_options = [
        "Magic: The Gathering", "Flesh & Blood",
        "Lorcana", "Pokemon", "Yu-Gi-Oh"
    ]
    first_names = ["John", "Jane", "Bob", "Alice", "Mike", "Sarah", "David", "Lisa"]
    last_names = ["Smith", "Jones", "Williams", "Brown", "Taylor", "Davies", "Wilson"]

    first_name = random.choice(first_names)
    last_name = random.choice(last_names)
    username = f"{first_name.lower()}_{last_name.lower()}_{random.randint(1, 999)}"

    user = User.objects.create_user(
        username=username,
        email=f"{username}@example.com",
        password='your_password_here',
        first_name=first_name,
        last_name=last_name
    )

    player = user.player  # This exists because of the signal
    player.phone_number = f"555-{random.randint(1000, 9999)}"
    player.preferred_game = random.choice(preferred_game_options)
    player.save()

    return player

def run_seed(self, mode):
    """Seed database based on mode"""
    clear_data()
    if mode == MODE_CLEAR:
        return

    for i in range(15):
        create_player()