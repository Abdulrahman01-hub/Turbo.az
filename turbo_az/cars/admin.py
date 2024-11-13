from django.contrib import admin
from .models import Car

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'year', 'price', 'condition', 'seller', 'date_posted')
    list_filter = ('condition', 'transmission', 'fuel_type', 'city')
    search_fields = ('brand', 'model', 'year', 'seller__username')
