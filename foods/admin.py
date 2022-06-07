from django.contrib import admin

# Register your models here.

from .models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'photo_tag', 'price', 'rate', 'quantity']
    list_editable = ['price', 'rate', 'quantity']
    search_fields = ['name']
    ordering = ['name']
    date_hierarchy = 'pub_date'



admin.site.register(Food, FoodAdmin)
