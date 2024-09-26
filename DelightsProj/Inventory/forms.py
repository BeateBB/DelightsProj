from django.shortcuts import render
from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = "__all__"

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = '__all__'


