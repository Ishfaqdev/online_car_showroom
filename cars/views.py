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


def all_cars(request):
    return render(request, 'cars/cars_list.html')


def car_detail(request, car_id):
    car_detail = Car.objects.get(pk=car_id)
    context = {
        'car_detail': car_detail,
    }
    return render(request, 'cars/cars_detail.html', context)


def search_cars(request):
    return render(request, 'cars/search.html')


def about(request):
    return render(request, 'cars/about.html')


def services(request):
    return render(request, 'cars/services.html')


def contact(request):
    return render(request, 'cars/contact.html')
