# tests.py
# David Marin & Silas Curtis
# Last Updated: 5/6/2025
# Contains the tests for Mediary
# Includes simple test

from django.test import TestCase

# Create your tests here.

from django.test import TestCase, Client
from django.urls import reverse

class SimpleViewTests(TestCase):
    """
    Test a simple view to see if it passes.
    """
    def test_home_page_loads(self):
        client = Client()
        response = client.get(reverse('mediary:home'))
        self.assertEqual(response.status_code, 200)
