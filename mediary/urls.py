from django.urls import path
from . import views

app_name = 'mediary'

urlpatterns = [
    # Main page
    path('', views.home, name='home'),
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