from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import forms MenuForm, IngredientForm, RequirementForm, PurchaseForm
from django.views.generic import ListView
from django.views.generic.edit import DeleteView, CreateView, UpdateView


# Create your views here.

class IngredientsView(ListView):
    model = Ingredient
    template_name = "Inventory/ingredient_list.html"

class CreateIngredientView(CreateView):
    model = Ingredient
    template_name = "Inventory/add_ingredient.html"
    form_class = IngredientForm

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = 'Ínventory/update_ingedient.html'
    form_class = IngredientForm

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = 'Inventory/delete_ingredient.html'
    success_url = '/ingredient_list'

class MenuView(ListView):
    model = MenuItem
    template_name = 'Inventory/menu.html'

class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = 'Inventory/add_menu_item.html'
    form_class = MenuForm

class UpdateMenuItemView(UpdateView):
    model = MenuItem
    template_name = 'Inventory/update_menu_item.html'
    form_class = MenuForm

class DeleteMenuItemView(DeleteView):
    model = MenuItem
    template_name = 'Inventory/delete_menu_item.html'
    success_url = '/menu'

class RequirementView(ListView):
    model = RecipeRequirement
    template_name = 'Inventory/requirement.html'

class CreateRequirementView(CreateView):
    model = RecipeRequirement
    template_name = 'Inventory/add_requirement.html'
    form_class = RequirementForm

class UpdateRequirementView(UpdateView):
    model = RecipeRequirement
    template_name = 'Inventory/update_requirement.html'
    form_class = RequirementForm

class DeleteRequirementView(DeleteView):
    model = RecipeRequirement
    template_name = 'Inventory/delete_requirement.html'
    success_url = '/requirement'

class PurchaseView(ListView):
    model = Purchase
    template_name = 'Inventory/purchase.html'

class CreatePurchaseView(CreateView):
    model = Purchase
    template_name = 'Inventory/add_purchase.html'
    form_class = PurchaseForm

class UpdatePurchaseView(UpdateView):
    model = Purchase
    template_name = 'Inventory/update_purchase.html'
    form_class = PurchaseForm

class DeletePurchaseView(DeleteView):
    model = Purchase
    template_name = 'Inventory/delete_purchase.html'
    success_url = '/purchase'