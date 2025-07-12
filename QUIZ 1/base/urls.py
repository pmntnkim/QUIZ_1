from django.urls import path
from .import views
from .views import about, home

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', about, name='about'),


]