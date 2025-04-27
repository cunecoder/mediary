# views.py
# David Marin & Silas Curtis
# 4/22/2025

from django.shortcuts import render

def home(request):
    return render(request, 'mediary/home.html')

def create_event(request):
    return render(request, 'mediary/create_event.html')