from django.urls import path
from .import views

app_name = 'inquiry'
urlpatterns = [
    path('inquiry', views.inquiry, name='inquiry'),

]
