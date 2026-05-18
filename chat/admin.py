from django.contrib import admin

from .models import Message


# Registra model no admin
admin.site.register(Message)