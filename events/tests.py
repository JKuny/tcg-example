from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone
import datetime

from events.models import Event


class EventValidationTests(TestCase):
    def setUp(self):
        self.event = Event.objects.create(
            organizer=None,
            game_name="Test Game",
            start_date=timezone.now().date() + datetime.timedelta(days=1),
            start_time=timezone.now().time(),
            end_time=(timezone.now() + datetime.timedelta(hours=2)).time(),
            player_spaces=4,
            description="Test description",
            rules="Test rules",
            price=10.00,
        )

    def test_event_cant_be_made_in_the_past(self):
        past_date = timezone.now().date() - datetime.timedelta(days=1)
        self.event.start_date = past_date

        with self.assertRaises(ValidationError):
            self.event.full_clean()

    def test_event_can_be_made_in_future(self):
        future_date = timezone.now() + datetime.timedelta(days=1)
        self.event.start_date = future_date.date()

        try:
            self.event.full_clean()
        except ValidationError as e:
            self.fail(f"Validation error was raised for future date: {str(e)}")
