from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import EventForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Event
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def home(request):
    return render(request, 'mediary/home.html')

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            return redirect("mediary:event_detail", event_id=instance.pk)
        return render(request, 'mediary/event_create.html', {"form": form})
    else:
        form = EventForm()
        return render(request, 'mediary/event_create.html', {"form": form})

@login_required
def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.user != event.user and not request.user.is_superuser:
        messages.error(request, "You do not have permission to delete this event.")
        return redirect('mediary:event_detail', event_id=event.id)
    if request.method == "POST":
        event.delete()
        messages.success(request, "Event deleted successfully.")
        return redirect('mediary:event_list')
    return redirect('mediary:event_detail', event_id=event.id)

def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    context = {'event': event}
    return render(request, 'mediary/event_detail.html', context)

def event_list(request):
    events = Event.objects.all().order_by('-created_at')
    form = EventForm()
    context = {'events': events, 'form': form}
    return render(request, 'mediary/all_events.html', context)

def about_us(request):
    return render(request, 'mediary/about_us.html')

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("mediary:home")
        return render(request, 'mediary/register.html', {"form": form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'mediary/register.html', {"form": form})

def user_login(request):
    if request.method == "POST":
        form = CustomAuthenticationForm(data=request.POST)
        print("Form data:", request.POST)
        print("Form is valid:", form.is_valid())
        print("Form errors:", form.errors)
        if form.is_valid():
            user = form.get_user()
            print("Authenticated user:", user)
            login(request, user)
            return redirect("mediary:home")
        print("Authentication failed")
        messages.error(request, "Invalid email or password.")
        return render(request, 'mediary/login.html', {"form": form})
    else:
        form = CustomAuthenticationForm()
        return render(request, 'mediary/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect("mediary:home")