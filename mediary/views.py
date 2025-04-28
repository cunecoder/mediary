# views.py
# David Marin & Silas Curtis
# 4/22/2025

from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from .forms import EventForm
from .models import Event
from django.http import HttpResponse
from django.template.loader import render_to_string





def home(request):
    return render(request, 'mediary/home.html')

def event_create(request):
    if request.method == "POST":
        form = EventForm(request.POST)

        if form.is_valid():
            instance = form.save()
            return redirect("mediary:event_detail",event_id=instance.pk)
        
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
    # Get the specific event or return a 404 if it doesn't exist
    event = get_object_or_404(Event, id=event_id)
    
    # Pass the event to the template context
    context = {'event': event}
    print(context)
    # Render the event details page
    return render(request, 'mediary/event_detail.html', context)


def event_list(request):
    """
    Render the profile page with events.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered page with all events.
    """
    # Get all events
    events = Event.objects.all().order_by('-created_at')
    form = EventForm()
    context = {'events': events, 'form': form}  # Changed 'events_list' to 'events'
    return render(request, 'mediary/all_events.html', context)
