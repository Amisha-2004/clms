from django.contrib import admin

# Register your models here.
# admin.py
from .models import Item

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'location', 'status', 'company')  # Columns to display in admin
    search_fields = ('name', 'category', 'location')  # Add search functionality
    list_filter = ('status', 'category')  # Add filtering options

#usage.py
from .models import Usage

@admin.register(Usage)
class UsageAdmin(admin.ModelAdmin):
    list_display = ('usageid', 'date', 'time', 'batch', 'quantity', 'itemid')
    search_fields = ('batch', 'itemid__name')  # Enable searching by batch or item name
    list_filter = ('date', 'itemid')  # Enable filtering by date or item
