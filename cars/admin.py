from django.contrib import admin
from django.forms import CheckboxSelectMultiple
from django.db import models
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


class CarAdmin(admin.ModelAdmin):

    formfield_overrides = {
        models.ManyToManyField: {'widget': CheckboxSelectMultiple},
    }


admin.site.register(Car, CarAdmin)
