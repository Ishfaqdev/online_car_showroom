from django.contrib.auth.tokens import default_token_generator, PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.urls import reverse
from django.conf import settings
from django.contrib.auth import login
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, redirect
from .forms import SignupForm
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import ContactForm
from .models import ContactMessage


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact_message = ContactMessage(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                phone=form.cleaned_data['phone'],
                message=form.cleaned_data['message']
            )
            contact_message.save()
            html_message = render_to_string('accounts/email_contact.html', {
                'sender_name': form.cleaned_data['name'],
                'sender_email': form.cleaned_data['email'],
                'sender_phone': form.cleaned_data['phone'],
                'message': form.cleaned_data['message'],
            })
            send_mail(
                'New Contact Message',
                f'You have received a new message from {form.cleaned_data["name"]}: {form.cleaned_data["message"]}',
                'ishfaq.bcs09@gmail.com',
                ['ishfaq.bcs09@gmail.com'],
                fail_silently=False,
                html_message=html_message,
            )

            messages.success(
                request, 'Thank you for contacting us. we will get back to you shortly!')

            return redirect('accounts:contact')
    else:
        form = ContactForm()

    return render(request, 'cars/contact.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Directly log in the user after signup
            login(request, user)
            messages.success(
                request, 'Account created successfully. You are now logged in.')
            return redirect('accounts:login')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(
                request, 'Login successfully.')
            return redirect('cars:home')
        else:
            # Add an error message
            messages.error(request, 'Invalid username or password.')

    return render(request, 'accounts/login.html')
