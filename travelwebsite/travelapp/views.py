

# Create your views here.
from django.shortcuts import render

def home(request):
    return render(request, 'travelapp/home.html')

def about(request):
    return render(request, 'travelapp/about.html')

def tours(request):
    return render(request, 'travelapp/tours.html')

def destinations(request):
    return render(request, 'travelapp/destinations.html')

def book_trip(request):
    return render(request, 'travelapp/book.html')
