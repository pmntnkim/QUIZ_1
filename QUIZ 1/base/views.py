from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base/home.html')

# QUIZ 1/base/views.py

from django.shortcuts import render

def home(request):
    # This tour guide will show the 'home.html' page
    return render(request, 'base/home.html')

def about(request):
    # This new tour guide will show the 'about.html' page
    return render(request, 'base/about.html')