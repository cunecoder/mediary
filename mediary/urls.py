# urls.py
# David Marin & Silas Curtis
# URLS for Mediary app
# 4/22/2025

"""
URL configuration for the Mediary app
"""
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mediary'

urlpatterns = [
    # Main page
    path('', views.home, name='home'),
    # Create event
    path('create/event', views.create_event, name='create_event')
    path('event/<int:event_id>', views.)
    ]
