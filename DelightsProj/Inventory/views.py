from typing import Any
from django.shortcuts import render
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, DaySummary, Day
from .forms import MenuForm, IngredientForm, RequirementForm, PurchaseForm
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

# Create your views here.


class HomeView(TemplateView):
    template_name = 'Inventory/home.html'
    model = Day

    def get_context_data(self):
        context = super().get_context_data()
        context['days'] = Day.objects.all()
        return context
    
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'

class DaySummaryView(TemplateView):
    template_name = 'Inventory/day_summary.html'
    model = DaySummary
    
    def get_context_data(self):
        context = super().get_context_data()
        context['summary'] = DaySummary.objects.first()
        return context

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
    success_url = '/ingredients'

class UpdateIngredientView(UpdateView):
    model = Ingredient
    template_name = 'Inventory/update_ingredient.html'
    form_class = IngredientForm
    success_url = '/ingredients'

class DeleteIngredientView(DeleteView):
    model = Ingredient
    template_name = 'Inventory/delete_ingredient.html'
    success_url = '/ingredients'
    

class MenuView(LoginRequiredMixin,ListView):
    model = MenuItem
    template_name = 'Inventory/menu.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['menu'] = MenuItem.objects.all()
        return context

class CreateMenuItemView(LoginRequiredMixin,CreateView):
    model = MenuItem
    template_name = 'Inventory/add_menu_item.html'
    form_class = MenuForm
    success_url='/menu'

class UpdateMenuItemView(UpdateView):
    model = MenuItem
    template_name = 'Inventory/update_menu_item.html'
    form_class = MenuForm
    success_url='/menu'

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
    success_url='/requirements'

class UpdateRequirementView(UpdateView):
    model = RecipeRequirement
    template_name = 'Inventory/update_requirement.html'
    form_class = RequirementForm
    success_url='/requirements'

class DeleteRequirementView(DeleteView):
    model = RecipeRequirement
    template_name = 'Inventory/delete_requirement.html'
    success_url='/requirements'


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
    success_url='/purchases'

class UpdatePurchaseView(UpdateView):
    model = Purchase
    template_name = 'Inventory/update_purchase.html'
    form_class = PurchaseForm
    success_url='/purchases'

class DeletePurchaseView(DeleteView):
    model = Purchase
    template_name = 'Inventory/delete_purchase.html'
    success_url='/purchases'

