from django.contrib import admin
from .models import MouseClick


@admin.register(MouseClick)
class MouseClickAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'timestamp')
    list_filter = ('timestamp',)
