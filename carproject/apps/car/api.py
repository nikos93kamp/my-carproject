import json

from django.db.models import Q
from django.http import JsonResponse

from .models import Car


def api_search(request):
    carslist = []
    data = json.loads(request.body)
    query = data['query']
    fuel_type = data['fuel_type']

    cars = Car.objects.filter(Q(brand__icontains=query) | Q(model__icontains=query) | Q(engine_size__icontains=query) | Q(horsepower__icontains=query) | Q(is_hybrid__icontains=query))

    if fuel_type:
        cars = cars.filter(fuel_type=fuel_type)

    for car in cars:
        obj = {
            'id': car.id,
            'brand': car.brand,
            'model': car.model,
            'url': '/cars/%s/' % car.id
        }
        carslist.append(obj)

    return JsonResponse({'cars': carslist})
