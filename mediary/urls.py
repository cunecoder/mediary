from django.urls import path
from . import views

app_name = 'mediary'

urlpatterns = [
    path('', views.home, name='home'),
    path('event/create/', views.event_create, name='event_create'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    path('event/<int:event_id>/delete/', views.delete_event, name='delete_event'),
    path('events/', views.event_list, name='event_list'),
    path('about/', views.about_us, name='about_us'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]