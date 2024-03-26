from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Inquiry
from urllib.parse import urlencode
from django.core.mail import send_mail
from django.contrib.auth.models import User


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        Inquiry_instance = Inquiry(
            car_id=car_id, car_title=car_title, user_id=user_id,
            first_name=first_name, last_name=last_name,
            customer_need=customer_need, city=city, state=state,
            email=email, phone=phone, message=message
        )

        # Save the contact instance to the database
        Inquiry_instance.save()

        return redirect('/car_details' + car_id)
