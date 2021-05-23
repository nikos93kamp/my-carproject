from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import AddCarForm, DealershipForm
from .models import Car

from apps.notification.utilities import create_notification


def search(request):
    return render(request, 'car/search.html')


def car_detail(request, car_id):
    car = Car.objects.get(pk=car_id)

    return render(request, 'car/car_detail.html', {'car': car})


@login_required
def entry_for_car(request, car_id):
    car = Car.objects.get(pk=car_id)

    if request.method == 'POST':
        form = DealershipForm(request.POST)

        if form.is_valid():
            dealership = form.save(commit=False)
            dealership.car = car
            dealership.created_by = request.user
            dealership.save()

            create_notification(request, car.created_by, 'dealership', extra_id=dealership.id)

            return redirect('dashboard')
    else:
        form = DealershipForm()

    return render(request, 'car/entry_for_car.html', {'form': form, 'car': car})


@login_required
def add_car(request):
    if request.method == 'POST':
        form = AddCarForm(request.POST)

        if form.is_valid():
            car = form.save(commit=False)
            car.created_by = request.user
            car.save()

            return redirect('dashboard')
    else:
        form = AddCarForm()

    return render(request, 'car/add_car.html', {'form': form})


@login_required
def edit_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id, created_by=request.user)

    if request.method == 'POST':
        form = AddCarForm(request.POST, instance=car)

        if form.is_valid():
            car = form.save(commit=False)
            car.created_by = request.user
            car.save()

            return redirect('dashboard')
    else:
        form = AddCarForm(instance=car)

    return render(request, 'car/edit_car.html', {'form': form, 'car': car})
