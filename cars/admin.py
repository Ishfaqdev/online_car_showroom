from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
from django import forms


from .models import Make, Color, Images, Features, Transmission, Model, Condition, Fuel_type, States, City, Car


@admin.register(Make)
class MakeAdmin(admin.ModelAdmin):
    pass


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    pass


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    pass


@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    pass


@admin.register(Transmission)
class TransmissionAdmin(admin.ModelAdmin):
    pass


@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    pass


@admin.register(Fuel_type)
class FuelTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(States)
class StatesAdmin(admin.ModelAdmin):
    pass


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    pass


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['car_images'].queryset = Images.objects.filter(
                car=instance)


class CarAdmin(admin.ModelAdmin):
    form = CarForm
    filter_horizontal = ('car_feature',)

    def formfield_for_manytomany(self, db_field, request, **kwargs):
        if db_field.name == "car_feature":
            kwargs["widget"] = CheckboxSelectMultiple()
        return super().formfield_for_manytomany(db_field, request, **kwargs)


admin.site.register(Car, CarAdmin)
