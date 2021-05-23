from django import forms

from .models import Car, Dealership


class AddCarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['brand', 'model', 'engine_size', 'horsepower',
                  'fuel_type', 'is_hybrid']


class DealershipForm(forms.ModelForm):
    class Meta:
        model = Dealership
        fields = ['name', 'address']
