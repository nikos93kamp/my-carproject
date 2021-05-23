from django.contrib.auth.models import User
from django.db import models


class Car(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    engine_size = models.CharField(max_length=100)
    horsepower = models.CharField(max_length=100)

    Gasoline = 'gasoline'
    Diesel = 'diesel'

    FuelType = (
        (Gasoline, 'gasoline'),
        (Diesel, 'diesel'),
    )

    fuel_type = models.CharField(default=Gasoline, choices=FuelType, max_length=20)
    is_hybrid = models.BooleanField(blank=True)

    created_by = models.ForeignKey(User, related_name='cars', on_delete=models.CASCADE)

    def __str__(self):
        return self.brand


class Dealership(models.Model):
    car = models.ForeignKey(Car, related_name='dealerships', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    created_by = models.ForeignKey(User, related_name='dealerships', on_delete=models.CASCADE)
