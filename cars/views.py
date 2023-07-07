from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):
    featured_cars = Car.objects.order_by(
        'created_date').filter(is_feature=True)
    context = {
        'featured_cars': featured_cars,
    }
    return render(request, 'cars/home.html', context)


def car_detail(request):
    return render(request, 'cars/car-details.html')


def about(request):
    return render(request, 'cars/about.html')


def services(request):
    return render(request, 'cars/services.html')


def contact(request):
    return render(request, 'cars/contact.html')
