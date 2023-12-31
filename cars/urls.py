from django.urls import path
from . import views
app_name = 'cars'
urlpatterns = [
    path('', views.home, name='home'),
    path('car_details/<int:car_id>/', views.car_detail, name='car_details'),
    path('all_cars', views.all_cars, name='all_cars'),
    path('search_cars', views.search_cars, name='search_cars'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('services/', views.services, name='services'),
]
