from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class Player(models.Model):
    # Create a django.contrib.auth.models.User
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add own fields to customize the user
    phone_number = models.CharField(max_length=15, blank=True)
    preferred_game = models.CharField(max_length=24, blank=True)
    profile_picture = models.ImageField(upload_to="profile_pictures", blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


@receiver(post_save, sender=User)
def create_player(sender, instance, created, **kwargs):
    if created:
        Player.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_player(sender, instance, **kwargs):
    instance.player.save()
