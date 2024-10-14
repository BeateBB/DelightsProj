from django.contrib import admin

# Register your models here.
from .models import Ingredient, RecipeRequirement, MenuItem, Purchase, DaySummary

admin.site.register(Ingredient)
admin.site.register(RecipeRequirement)
admin.site.register(MenuItem)
admin.site.register(Purchase)
admin.site.register(DaySummary)
