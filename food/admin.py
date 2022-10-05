from django.contrib import admin

from .models import Food, Nutrient, FoodNutrients

admin.site.register(Food)
admin.site.register(Nutrient)
admin.site.register(FoodNutrients)