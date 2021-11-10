from django.contrib import admin
from myapp.models import Player

# Register your models here.

@admin.register(Player)

class PlayerAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'jersey_no', 'role']
