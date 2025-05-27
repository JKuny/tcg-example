from django.db import models


class Event(models.Model):
    organizer = models.ForeignKey(
        'players.Organizer',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='events'
    )
    game_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')
    start_time = models.TimeField('time started')
    end_time = models.TimeField('time ended')
    player_spaces = models.IntegerField()
    description = models.TextField()
    rules = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
