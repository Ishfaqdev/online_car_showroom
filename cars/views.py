from django.shortcuts import render
from django.db.models import Q
from datetime import datetime, timedelta
from .models import *
from .forms import CarSearchForm
# Create your views here.


def home(request):
    featured_cars = Car.objects.order_by(
        'created_date').filter(is_feature=True)

    latest_cars = Car.objects.order_by('created_date')[:6]

    # Get the search keyword from the query parameters
    keyword = request.GET.get('keyword', '')

    search_results = Car.objects.filter(
        Q(car_title__icontains=keyword) |
        Q(car_description__icontains=keyword) |
        Q(car_make__car_make__icontains=keyword) |
        Q(car_model__icontains=keyword) |
        Q(body_style__icontains=keyword)
    ).order_by('-created_date')

    context = {
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
        'search_results': search_results,
        'keyword': keyword,  # Pass the keyword back to the template for display
    }

    context = {
        'featured_cars': featured_cars,
        'latest_cars': latest_cars,
    }
    return render(request, 'cars/home.html', context)


def all_cars(request):
    all_cars = Car.objects.all()
    make_search = Car.objects.values_list(
        'car_make__car_make', flat=True).distinct()
    model_search = Car.objects.values_list('car_model', flat=True).distinct()
    city_search = Car.objects.values_list(
        'car_city__city', flat=True).distinct()
    year_search = Car.objects.values_list('car_year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list(
        'car_transmission__car_transmissions', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            all_cars = all_cars.filter(Q(car_description__icontains=keyword) | Q(
                car_title__icontains=keyword))

    if 'make' in request.GET:
        make = request.GET['make']
        print("Selected Make:", make)
        if make:
            all_cars = all_cars.filter(car_make__car_make__iexact=make)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            all_cars = all_cars.filter(car_model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            all_cars = all_cars.filter(car_city__city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            all_cars = all_cars.filter(car_year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = all_cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            all_cars = all_cars.filter(
                car_transmission__car_transmissions__iexact=transmission)

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price and min_price:
            all_cars = all_cars.filter(car_price__gte=min_price,
                                       car_price__lte=max_price)

    data = {
        'all_cars': all_cars,
        'make_search': make_search,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search
    }
    return render(request, 'cars/cars_list.html', data)


def car_details(request, car_id):
    car_detail = Car.objects.get(pk=car_id)
    features = Features.objects.all()
    related_cars = Car.objects.filter(
        car_make=car_detail.car_make).exclude(pk=car_id)[:4]
    make_search = Car.objects.values_list(
        'car_make__car_make', flat=True).distinct()
    model_search = Car.objects.values_list('car_model', flat=True).distinct()
    city_search = Car.objects.values_list(
        'car_city__city', flat=True).distinct()
    year_search = Car.objects.values_list('car_year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list(
        'car_transmission__car_transmissions', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(Q(car_description__icontains=keyword) | Q(
                car_title__icontains=keyword))

    if 'make' in request.GET:
        make = request.GET['make']
        print("Selected Make:", make)
        if make:
            cars = cars.filter(car_make__car_make__iexact=make)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(car_model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(car_city__city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(car_year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(
                car_transmission__car_transmissions__iexact=transmission)

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price and min_price:
            cars = cars.filter(car_price__gte=min_price,
                               car_price__lte=max_price)
    context = {
        'car_detail': car_detail,
        'features': features,
        'related_cars': related_cars,
        'make_search': make_search,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search
    }
    return render(request, 'cars/cars_detail.html', context)


def search_cars(request):
    cars = Car.objects.all()

    make_search = Car.objects.values_list(
        'car_make__car_make', flat=True).distinct()
    model_search = Car.objects.values_list('car_model', flat=True).distinct()
    city_search = Car.objects.values_list(
        'car_city__city', flat=True).distinct()
    year_search = Car.objects.values_list('car_year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list(
        'car_transmission__car_transmissions', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(Q(car_description__icontains=keyword) | Q(
                car_title__icontains=keyword))

    if 'make' in request.GET:
        make = request.GET['make']
        print("Selected Make:", make)
        if make:
            cars = cars.filter(car_make__car_make__iexact=make)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(car_model__iexact=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(car_city__city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(car_year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(
                car_transmission__car_transmissions__iexact=transmission)

    if 'min_price' in request.GET and 'max_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price and min_price:
            cars = cars.filter(car_price__gte=min_price,
                               car_price__lte=max_price)

    data = {
        'cars': cars,
        'make_search': make_search,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
        'transmission_search': transmission_search
    }

    return render(request, 'cars/search.html', data)


def about(request):
    return render(request, 'cars/about.html')


def services(request):
    return render(request, 'cars/services.html')
