from typing import Any
from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase
from .forms import MenuForm, IngredientForm, RequirementForm, PurchaseForm
from django.views.generic import ListView, TemplateView
from django.views.generic.edit import DeleteView, CreateView, UpdateView


# Create your views here.


class HomeView(TemplateView):
    template_name = 'Inventory/home.html'

class IngredientsView(ListView):
    model = Ingredient
    template_name = "Inventory/ingredient_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        context['ingredients'] = Ingredient.objects.all()
        return context
   

class CreateIngredientView(CreateView):
    model = Ingredient
    template_name = "Inventory/add_ingredient.html"
    form_class = IngredientForm
    success_url = 'ingredient_list.html'

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

    def get_context_data(self):
        context = super().get_context_data()
        context['menu'] = MenuItem.objects.all()
        return context

class CreateMenuItemView(CreateView):
    model = MenuItem
    template_name = 'Inventory/add_menu_item.html'
    form_class = MenuForm
    success_url='menu.html'

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

    def get_context_data(self):
        context = super().get_context_data()
        context['requirements'] = RecipeRequirement.objects.all()
        return context

class CreateRequirementView(CreateView):
    model = RecipeRequirement
    template_name = 'Inventory/add_requirement.html'
    form_class = RequirementForm
    success_url='requirement.html'

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

    def get_context_data(self):
        context = super().get_context_data()
        context['purchases'] = Purchase.objects.all()
        return context

class CreatePurchaseView(CreateView):
    model = Purchase
    template_name = 'Inventory/add_purchase.html'
    form_class = PurchaseForm
    success_url='purchase.html'

class UpdatePurchaseView(UpdateView):
    model = Purchase
    template_name = 'Inventory/update_purchase.html'
    form_class = PurchaseForm

class DeletePurchaseView(DeleteView):
    model = Purchase
    template_name = 'Inventory/delete_purchase.html'
    success_url = '/purchase'