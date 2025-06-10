from django.db import models

from events.validators import validate_future_date
from players.models import Player


class Event(models.Model):
    organizer = models.ForeignKey(
        Player,
        on_delete=models.SET_NULL,
        related_name="organized_events",
        null=True,
        blank=True,
    )
    game_name = models.CharField(max_length=200)
    start_date = models.DateField("date started", validators=[validate_future_date])
    start_time = models.TimeField("time started")
    end_time = models.TimeField("time ended")
    player_spaces = models.IntegerField()
    description = models.TextField()
    rules = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    participants = models.ManyToManyField(
        Player, through="EventParticipation", related_name="participating_events"
    )

    def __str__(self):
        return f"{self.game_name} - {self.rules}"


class EventParticipation(models.Model):
    """
    Intermediary model for the many-to-many relationship between Player and Event.
    This allows you to store additional information about the participation.
    """

    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)
    notes = models.TextField(blank=True)

    class Meta:
        # Ensure a player can't be registered for the same event twice
        unique_together = ["player", "event"]
        ordering = ["registration_date"]

    def __str__(self):
        return f"{self.player} - {self.event}"


class EventParticipant(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    registration_date = models.DateTimeField(auto_now_add=True)
    attended = models.BooleanField(default=False)

    class Meta:
        unique_together = ["player", "event"]
        ordering = ["registration_date"]

    def __str__(self):
        return f"{self.player} - {self.event}"
