from django.db import models
from datetime import datetime


class Make(models.Model):
    car_make = models.CharField(max_length=55)

    def __str__(self):
        return self.car_make


class Images(models.Model):
    car_image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return str(self.car_image)


class Color(models.Model):
    car_color = models.CharField(max_length=55)

    def __str__(self):
        return self.car_color


class Features(models.Model):
    car_features = models.CharField(max_length=100)

    def __str__(self):
        return self.car_features


class Transmission(models.Model):
    car_transmissions = models.CharField(max_length=55)

    def __str__(self):
        return self.car_transmissions


class Model(models.Model):
    car_model = models.CharField(max_length=55)

    def __str__(self):
        return self.car_model


class Condition(models.Model):
    car_condition = models.CharField(max_length=55)

    def __str__(self):
        return self.car_condition


class Fuel_type(models.Model):
    car_fuel = models.CharField(max_length=55)

    def __str__(self):
        return self.car_fuel


class States(models.Model):
    state = models.CharField(max_length=100)

    def __str__(self):
        return self.state


class City(models.Model):
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.city


year_choice = []
for r in range(1980, (datetime.now().year+1)):
    year_choice.append((r, r))

STATUS_CHOICES = (
    ('available', 'available'),
    ('reserved', 'reserved'),
    ('sold', 'sold'),
)


class Car(models.Model):
    car_title = models.CharField(max_length=55)
    car_make = models.ForeignKey(Make, on_delete=models.CASCADE)
    car_color = models.ForeignKey(Color, on_delete=models.CASCADE)
    car_model = models.ForeignKey(Model, on_delete=models.CASCADE)
    car_states = models.ForeignKey(States, on_delete=models.CASCADE)
    car_city = models.ForeignKey(City, on_delete=models.CASCADE)
    car_transmission = models.ForeignKey(
        Transmission, on_delete=models.CASCADE)
    car_year = models.IntegerField(('year'), choices=year_choice)
    car_condition = models.ForeignKey(Condition, on_delete=models.CASCADE)
    car_fuel_type = models.ForeignKey(Fuel_type, on_delete=models.CASCADE)
    car_price = models.IntegerField()
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.IntegerField()
    pessengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    milage = models.IntegerField()
    no_of_owners = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='available')
    is_feature = models.BooleanField(default=False)
    car_images = models.ManyToManyField('Images', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    car_description = models.TextField()
    car_feature = models.ManyToManyField(Features)

    def __str__(self):
        return self.car_title
