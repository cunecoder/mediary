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
    # Display all the events
    path('events/', views.event_list, name='event_list'),
    # Create event
    path('events/create/', views.event_create, name='event_create'),
    # Display a specific event based on it's id
    path('events/<int:event_id>', views.event_detail, name="event_detail"),
    # About us page
    path('aboutus/', views.about_us, name='about_us')
    ]
