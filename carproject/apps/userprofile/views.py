from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from apps.car.models import Car, Dealership
from .models import ConversationMessage
from apps.notification.utilities import create_notification


@login_required
def dashboard(request):
    return render(request, 'userprofile/dashboard.html', {'userprofile': request.user.userprofile})


@login_required()
def view_dealership(request, dealership_id):
    if request.user.userprofile.is_manager:
        dealership = get_object_or_404(Dealership, pk=dealership_id, car__created_by=request.user)
    else:
        dealership = get_object_or_404(Dealership, pk=dealership_id, created_by=request.user)

    if request.method == 'POST':
        content = request.POST.get('content')

        if content:
            conversationmessage = ConversationMessage.objects.create(dealership=dealership, content=content, created_by=request.user)

            create_notification(request, dealership.created_by, 'message', extra_id=dealership.id)

            return redirect('view_dealership', dealership_id=dealership_id)

    return render(request, 'userprofile/view_dealership.html', {'dealership': dealership})


@login_required
def view_dashboard_car(request, car_id):
    car = get_object_or_404(Car, pk=car_id, created_by=request.user)

    return render(request, 'userprofile/view_dashboard_car.html', {'car': car})
