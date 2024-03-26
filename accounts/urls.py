from django.urls import path
from . import views
app_name = 'accounts'
urlpatterns = [
    path('login', views.login_page, name='login'),
    path('signup', views.signup, name='signup'),

    path('contact', views.contact, name='contact'),

]
