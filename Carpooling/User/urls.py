from django.urls import path, re_path
from .views import *
from django.shortcuts import redirect

urlpatterns = [
    path("Registeration/",  UserRegister, name="register"),
    path('Add-Car/', AddCar, name='add_car'),
    path('Profile/',UserProfile, name='Profile'),
    path('My-Rides/',UserRide, name='My_rides'),
    path('Add-License/',AddLicense, name='Add_license'),
    path('About/',About,name="About"),
    re_path(r'search/',Search),
]
