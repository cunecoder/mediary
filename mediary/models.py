# models.py
# David Marin & Silas Curtis
# Last Updated: 5/6/2025
# Models for mediary app. 
# Includes: User, Event, UserModelTests


from django.contrib.auth.models import AbstractUser, UserManager as BaseUserManager
from django.db import models
from django.conf import settings
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email="test@example.com", password="secret")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("secret"))

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