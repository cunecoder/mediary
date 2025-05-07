# tests.py
# David Marin & Silas Curtis
# Last Updated: 5/6/2025
# Contains the tests for Mediary
# Includes simple with self explanatory names. No need for docstrings.


from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from .models import Event, User
from datetime import timedelta

class UserAuthTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='testuser@example.com', username='testuser', password='password123')
        self.client = Client()

    def test_user_login_success(self):
        response = self.client.post(reverse('mediary:login'), {
            'username': 'testuser@example.com',
            'password': 'password123'
        })
        self.assertRedirects(response, reverse('mediary:home'))

    def test_user_login_fail(self):
        response = self.client.post(reverse('mediary:login'), {
            'username': 'testuser@example.com',
            'password': 'wrongpass'
        })
        self.assertContains(response, "Invalid email or password.")

    def test_user_register(self):
        response = self.client.post(reverse('mediary:register'), {
            'username': 'newuser',
            'email': 'new@example.com',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertRedirects(response, reverse('mediary:home'))
        self.assertTrue(User.objects.filter(email='new@example.com').exists())



class EventTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='eventuser@example.com', username='eventuser', password='password123')
        self.event = Event.objects.create(
            user=self.user,
            title='Test Event',
            location='Test Location',
            description='Test Description',
            time=timezone.now() + timedelta(days=1)
        )

    def test_event_list_view(self):
        response = self.client.get(reverse('mediary:event_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_event_detail_view(self):
        response = self.client.get(reverse('mediary:event_detail', args=[self.event.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.event.title)

    def test_event_create_logged_in(self):
        self.client.login(email='eventuser@example.com', password='password123')
        response = self.client.post(reverse('mediary:event_create'), {
            'title': 'New Event',
            'location': 'New Location',
            'description': 'New Description',
            'time': timezone.now() + timedelta(days=2)
        })
        new_event = Event.objects.get(title='New Event')
        self.assertRedirects(response, reverse('mediary:event_detail', args=[new_event.id]))
        self.assertEqual(new_event.user, self.user)

    def test_event_create_unauthenticated_redirect(self):
        response = self.client.get(reverse('mediary:event_create'))
        self.assertRedirects(response, '/login/?next=' + reverse('mediary:event_create'))

    def test_event_delete_by_owner(self):
        self.client.login(email='eventuser@example.com', password='password123')
        response = self.client.post(reverse('mediary:delete_event', args=[self.event.id]))
        self.assertRedirects(response, reverse('mediary:event_list'))
        self.assertFalse(Event.objects.filter(id=self.event.id).exists())

    def test_event_delete_unauthorized_user(self):
        other_user = User.objects.create_user(email='other@example.com', username='otheruser', password='password456')
        self.client.login(email='other@example.com', password='password456')
        response = self.client.post(reverse('mediary:delete_event', args=[self.event.id]))
        self.assertRedirects(response, reverse('mediary:event_detail', args=[self.event.id]))
        self.assertTrue(Event.objects.filter(id=self.event.id).exists())


class EventModelTests(TestCase):
    def test_event_str_output(self):
        user = User.objects.create_user(email='a@a.com', username='a', password='pass')
        event = Event.objects.create(
            user=user,
            title='Sample Title',
            location='Sample Location',
            description='Sample Description',
            time=timezone.now()
        )
        output = str(event)
        self.assertIn('Sample Title', output)
        self.assertIn(user.email, output)
