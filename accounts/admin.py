from django.contrib import admin
from .models import ContactMessage


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'timestamp')
    list_filter = ('timestamp',)
    search_fields = ('name', 'email', 'subject', 'message')


admin.site.register(ContactMessage, ContactMessageAdmin)
