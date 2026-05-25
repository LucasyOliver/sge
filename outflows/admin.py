from django.contrib import admin
from .models import Outflow


@admin.register(Outflow)
class OutflowAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity',)
    search_fields = ('product',)
