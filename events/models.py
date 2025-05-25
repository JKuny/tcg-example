from django.db import models


class Tournament(models.Model):
    """
    Represents a TCG tournament.
    """
    game_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('date started')
    start_time = models.TimeField('time started')
    player_spaces = models.IntegerField()
    description = models.TextField()
    rules = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    prizes = models.TextField()
