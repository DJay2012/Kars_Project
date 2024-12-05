#This file is not created automatically, we have to create it manually

from django.urls import path
from . import views

urlpatterns = [
    path ('', views.home, name='home'),
    path('add/', views.add_car, name='add_car'),
    path('delete/<int:car_id>/', views.delete_car, name='delete_car'),
]