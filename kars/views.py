from django.shortcuts import render, get_object_or_404, redirect
from .models import Kar  # Importing the Kar model from models.py
from .forms import KarForm  # Correcting the form name to match your Kar model

# View to add a new car
def add_car(request):
    if request.method == "POST":
        form = KarForm(request.POST, request.FILES)  # Ensure files like images are handled
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to the home page after saving
    else:
        form = KarForm()
    return render(request, 'add_car.html', {'form': form})

# View to delete an existing car
def delete_car(request, car_id):
    car = get_object_or_404(Kar, id=car_id)
    if request.method == "POST":
        car.delete()
        return redirect('home')  # Redirect to the home page after deletion
    return render(request, 'delete_car.html', {'car': car})

# Home view to display the list of cars
def home(request):
    cars = Kar.objects.all()  # Fetch all cars from the database
    return render(request, 'home.html', {'cars': cars})

# Detail view to display a specific car's details
def car_detail(request, car_id):
    car = get_object_or_404(Kar, pk=car_id)  # Fetch the car by primary key
    return render(request, 'car_detail.html', {'car': car})