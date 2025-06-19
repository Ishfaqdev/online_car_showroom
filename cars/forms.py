from django import forms
from .models import year_choice, Make, Transmission, Condition, Fuel_type, States, City


class CarSearchForm(forms.Form):
    select_brand = forms.ModelChoiceField(
        queryset=Make.objects.all(), empty_label="Select Make")
    select_make = forms.CharField(max_length=100, required=False)
    select_location = forms.ModelChoiceField(
        queryset=States.objects.all(), empty_label="Select Location")
    select_year = forms.ChoiceField(choices=year_choice, required=False)
    select_type = forms.ModelChoiceField(
        queryset=Condition.objects.all(), empty_label="Select Condition")
    min_price = forms.IntegerField(min_value=0, required=False)
    max_price = forms.IntegerField(min_value=0, required=False)
