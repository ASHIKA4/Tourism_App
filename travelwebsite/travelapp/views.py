

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'travelapp/home.html')

def about(request):
    return render(request, 'travelapp/about.html')

def service(request):
    return render(request, 'travelapp/service.html')

def tours(request):
    return render(request, 'travelapp/tours.html')

def destinations(request):
    return render(request, 'travelapp/destinations.html')

def book_trip(request):
    return render(request, 'travelapp/book.html')

import os
from django.conf import settings

def about(request):
    template_path = os.path.join(settings.BASE_DIR, 'travelapp', 'templates', 'travelapp', 'about.html')
    print(f"Checking if template exists: {os.path.exists(template_path)}")
    return render(request, 'travelapp/about.html')


