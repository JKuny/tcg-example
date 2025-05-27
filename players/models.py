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
    preferred_game = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True)


    def __str__(self):
        return "{self.user.first_name} {self.user.last_name}"


class Organizer(Player):
    class Meta:
        verbose_name = 'Organizer'
        verbose_name_plural = 'Organizers'


@receiver(post_save, sender=User)
def create_player(sender, instance, created, **kwargs):
    """
    Signal receiver function to create a Player instance when a new User instance is created.

    This function listens to the `post_save` signal triggered whenever a `User` instance is
    saved. If the `created` flag is True, indicating that a new `User` was created, it
    automatically creates a corresponding `Player` instance associated with the `User`.

    Parameters:
        sender (type): The model class that triggered the signal.
        instance (User): The instance of the User that was saved.
        created (bool): A boolean indicating if the instance was newly created.
        **kwargs (dict): Additional keyword arguments passed by the signal.
    """
    if created:
        Player.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_player(sender, instance, **kwargs):
    """
    Signal receiver function to save the Player instance associated with the User instance.
    This function is triggered after a User instance is saved to ensure the corresponding
    Player instance is also saved.

    Parameters:
        sender (type): The model class that sent the signal (User in this case).
        instance (User): The instance of the model that was saved.
        kwargs (dict): Additional keyword arguments provided by the signal.

    """
    instance.player.save()
