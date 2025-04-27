# models.py
# Author: David Marin & Silas Curtis
# Last Updated: 4/27/2025
# Description: This file contains the models we use for the Mediary website's database.
# * Includes: Events, Users

from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models

# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Event(models.Model):
    """
    Model representing an Event.

    Attributes:
        title       (CharField): Title of the event.
        location    (CharField now, maybe another type later):
        description (CharField)
        time        (DATETIMEFIELD LATER: CharField now)

        # Will implement user later ***user (ForeignKey): The user who created the chirp.        
        # might not need this, might add later (from chirper) created_at (DateTimeField): The timestamp when the event was created.
    """
    # copied from chirper, will use later maybe: user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    # might not need, from chirper, might add later: created_at = models.DateTimeField(auto_now_add=True)
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
            f"""\"{self.title}\"
            Location: {self.location}
            Description: {self.description}"""
        )