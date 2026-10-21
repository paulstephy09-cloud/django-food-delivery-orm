from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import FoodItem, FoodOrder

admin.site.register(FoodItem)
admin.site.register(FoodOrder)