from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from apps.car.models import Car
from apps.userprofile.models import Userprofile


def frontpage(request):
    cars = Car.objects.all()[0:3]

    return render(request, 'core/frontpage.html', {'cars': cars})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()

            account_type = request.POST.get('account_type', 'customer')

            if account_type == 'manager':
                userprofile = Userprofile.objects.create(user=user, is_manager=True)
                userprofile.save()
            else:
                userprofile = Userprofile.objects.create(user=user)
                userprofile.save()

            login(request, user)

            return redirect('dashboard')
    else:
        form = UserCreationForm()

    return render(request, 'core/signup.html', {'form': form})
