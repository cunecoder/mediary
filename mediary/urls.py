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
    path('about/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]