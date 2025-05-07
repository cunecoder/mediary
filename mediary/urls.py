# urls.py
# David Marin & Silas Curtis
# Last Updated: 5/6/2025
# Models for mediary app. 
# Includes: paths for home, all events, event creation, event detail,
#           about us, register, login, logout, event deletion

from django.urls import path
from . import views

app_name = 'mediary'

urlpatterns = [
    # Main page - added 'home/' because I wanted to be able to end the url with home :)
    path('', views.home, name='home'),
    path('home/', views.home, name='home_alt'),
    # Display all the events
    path('events/', views.event_list, name='event_list'),
    # Create event
    path('events/create/', views.event_create, name='event_create'),
    # Display a specific event based on its id
    path('events/<int:event_id>', views.event_detail, name="event_detail"),
    # About us page
    path('aboutus/', views.about_us, name='about_us'),
    # Authentication
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    # Delete event view
    path('events/<int:event_id>/delete/', views.delete_event, name='event_delete')
]