from django.urls import path
from . import views
app_name = 'cars'
urlpatterns = [
    path('about-us', views.about, name='about'),
    path('', views.home, name='home'),
    path('car_details/<int:car_id>', views.car_details, name='car_details'),
    path('all_cars', views.all_cars, name='all_cars'),
    path('search_cars', views.search_cars, name='search_cars'),
    path('services', views.services, name='services'),
]
