from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
import re


class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, error_messages={
        'required': 'Please enter your email address.'
    })

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',
                  'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['username'].required = True
        self.fields['password1'].required = True
        self.fields['password2'].required = True

        # Customize error messages for required fields
        self.fields['first_name'].error_messages['required'] = 'Please enter your first name.'
        self.fields['last_name'].error_messages['required'] = 'Please enter your last name.'
        self.fields['username'].error_messages['required'] = 'Please enter your user name.'
        self.fields['password1'].error_messages['required'] = 'Please enter your password.'
        self.fields['password2'].error_messages['required'] = 'Please confirm your password.'

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        if username.isdigit():
            raise forms.ValidationError(
                "Username must not be entirely numeric.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email is already associated with an account.")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        # Custom password validation
        if len(password1) < 8:
            raise forms.ValidationError(
                "Password must be at least 8 characters long.")
        if not re.search(r'[A-Za-z]', password1):
            raise forms.ValidationError(
                "Password must contain at least one letter.")
        if not re.search(r'\d', password1):
            raise forms.ValidationError(
                "Password must contain at least one digit.")
        if not re.search(r'[^A-Za-z0-9]', password1):
            raise forms.ValidationError(
                "Password must contain at least one special character.")

        return password2


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    phone = forms.CharField(max_length=15)
    message = forms.CharField(widget=forms.Textarea)
