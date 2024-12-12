from django.shortcuts import render
from django import forms
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Day


class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuItem
        fields = ('item_name','price')

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RequirementForm(forms.ModelForm):
    class Meta:
        model = RecipeRequirement
        fields = ('ingredient','quantity')

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = Purchase
        fields = ('customer_name', 'purchased_item', 'purchase_time', 'quantity')


class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ("is_open",)
        widgets = { 'is_open': forms.HiddenInput(),}

RecipeFormSet = forms.inlineformset_factory(MenuItem, RecipeRequirement, fields=['ingredient','quantity'], extra = 5)

class RecipeForm(forms.ModelForm):
    pass
        
