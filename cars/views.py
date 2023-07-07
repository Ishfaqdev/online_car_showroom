from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'cars/home.html')


def car_detail(request):
    return render(request, 'cars/car-details.html')


def about(request):
    return render(request, 'cars/about.html')


def services(request):
    return render(request, 'cars/services.html')


def contact(request):
    return render(request, 'cars/contact.html')
