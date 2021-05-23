from django.urls import path, include

from .views import dashboard, view_dealership, view_dashboard_car

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('car/<int:car_id>', view_dashboard_car, name='view_dashboard_car'),
    path('dealership/<int:dealership_id>/', view_dealership, name='view_dealership'),
]
