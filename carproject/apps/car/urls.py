from django.urls import path, include

from .api import api_search
from .views import add_car, car_detail, entry_for_car, search, edit_car

urlpatterns = [
    path('api/search', api_search, name='api_search'),
    path('search/', search, name='search'),
    path('add/', add_car, name='add_car'),
    path('<int:car_id>/', car_detail, name='car_detail'),
    path('<int:car_id>/edit/', edit_car, name='edit_car'),
    path('<int:car_id>/entry_for_car/', entry_for_car, name='entry_for_car'),
]
