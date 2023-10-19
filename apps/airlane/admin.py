from django.contrib import admin
from .models import *

@admin.register(Airlane)
class AirlaneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
