from django.contrib import admin
from .models import *

@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    list_display = ('id', 'From')
    list_display_links = ('id', 'From')
