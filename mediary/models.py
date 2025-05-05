from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Event(models.Model):
    """
    Model representing an Event.

    Attributes:
        title       (CharField): Title of the event.
        location    (CharField): Event location.
        description (CharField): Event description.
        time        (DateTimeField): Event date and time.
        user        (ForeignKey): The user who created the event.
        created_at  (DateTimeField): Timestamp when the event was created.
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        """
        String representation of the event model.

        Returns:
            str: A string representing the event.
        """
        return (
            f"""
            Title:     \"{self.title}\"
            Location:    {self.location}
            Description: {self.description}
            Time:        {self.time}
            Created by:  {self.user.email if self.user else 'Anonymous'}
        """
        )