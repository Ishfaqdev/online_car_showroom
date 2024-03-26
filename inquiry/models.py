from django.db import models
from datetime import datetime
from cars.models import *
from django.contrib.auth.models import User


class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    customer_need = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    message = models.TextField()
    inquiry_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return f"Inquiry for {self.car} by {self.user}"
