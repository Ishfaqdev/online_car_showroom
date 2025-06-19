from django.contrib import admin
from .models import Inquiry
# Register your models here.


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['user', 'car', 'customer_need',
                    'city', 'phone', 'inquiry_date']
    list_filter = ['inquiry_date']
    search_fields = ['user__username', 'car__car_title', 'phone']
    ordering = ['-inquiry_date']


admin.site.register(Inquiry, InquiryAdmin)
