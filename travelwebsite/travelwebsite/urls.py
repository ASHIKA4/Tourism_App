"""
URL configuration for travelwebsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from travelapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('service/', views.service, name='service'),
    path('pricing/', views.pricing, name='pricing'),
    path('tours/', views.tours, name='tours'),
    path('destination/', views.destination, name='destination'),
    path('questions/', views.questions, name='questions'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('book/', views.book_trip, name='book_trip'),
    path('contact/', views.contact, name='contact'),
]