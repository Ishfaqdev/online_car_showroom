from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('car_details', views.car_detail, name='car_detail'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
]
