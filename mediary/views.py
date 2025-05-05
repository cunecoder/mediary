from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import EventForm, CustomUserCreationForm, CustomAuthenticationForm
from .models import Event
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'mediary/home.html')

@login_required
def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user  # Associate the event with the logged-in user
            instance.save()
            return redirect("mediary:event_detail", event_id=instance.pk)
        return render(request, 'mediary/event_create.html', {"form": form})
    else:
        form = EventForm()
        return render(request, 'mediary/event_create.html', {"form": form})

def event_detail(request, event_id):
    """
    Render the page for a specific event.

    Args:
        request: The HTTP request object.
        event_id: The ID of the event.

    Returns:
        HttpResponse: The rendered page with the event details.
    """
    event = get_object_or_404(Event, id=event_id)
    context = {'event': event}
    return render(request, 'mediary/event_detail.html', context)

def event_list(request):
    """
    Render the page with all events.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered page with all events.
    """
    events = Event.objects.all().order_by('-created_at')
    form = EventForm()
    context = {'events': events, 'form': form}
    return render(request, 'mediary/all_events.html', context)

def about_us(request):
    """
    Render the 'About Us' page with info on Mediary.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered page.
    """
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
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("mediary:home")
        return render(request, 'mediary/login.html', {"form": form})
    else:
        form = CustomAuthenticationForm()
        return render(request, 'mediary/login.html', {"form": form})

def user_logout(request):
    logout(request)
    return redirect("mediary:home")