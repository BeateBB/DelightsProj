from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Ingredient, MenuItem, RecipeRequirement, Purchase, Day
from .forms import MenuForm, IngredientForm, RequirementForm, PurchaseForm, DayForm
from django.views.generic import ListView, TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from datetime import date
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def today_object():
    today_object, created = Day.objects.get_or_create(date = date.today())
    if created:
        yesterday = Day.objects.order_by('-pk')[1]
        yesterday.finish_day()
    return today_object


class HomeView(TemplateView):
    template_name = 'Inventory/home.html'
    model = Day

    def get_context_data(self):
        context = super().get_context_data()
        context['days'] = Day.objects.order_by('-pk')
        return context   

    
class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/sign_up.html'

class DaySummaryView(TemplateView):
    template_name = 'Inventory/day_summary.html'
    model = Day
    
    def get_context_data(self):
        context = super().get_context_data()
        today = today_object()
        context['ingredients'] = today.today_ingredients.all()
        context['summary'] = today
        return context

class IngredientsView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = "Inventory/ingredient_list.html"

    def get_context_data(self):
        context = super().get_context_data()
        today = today_object()
        context['ingredients'] = today.today_ingredients.all()
        return context
   

class CreateIngredientView(LoginRequiredMixin,CreateView):
    model = Ingredient
    template_name = "Inventory/add_ingredient.html"
    form_class = IngredientForm
    success_url = '/ingredients'

class UpdateIngredientView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    template_name = 'Inventory/update_ingredient.html'
    form_class = IngredientForm
    success_url = '/ingredients'

class DeleteIngredientView(LoginRequiredMixin, DeleteView):
    model = Ingredient
    template_name = 'Inventory/delete_ingredient.html'
    success_url = '/ingredients'
    

class MenuView(ListView):
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

class UpdateMenuItemView(LoginRequiredMixin, UpdateView):
    model = MenuItem
    template_name = 'Inventory/update_menu_item.html'
    form_class = MenuForm
    success_url='/menu'

class DeleteMenuItemView(LoginRequiredMixin, DeleteView):
    model = MenuItem
    template_name = 'Inventory/delete_menu_item.html'
    success_url = '/menu'

# RecipeRequiremet view for MenuItem
class RecipeDetailView(DetailView):
    model = MenuItem
    template_name = 'Inventory/recipe.html'
    context_object_name = 'MenuItem'

class RequirementView(ListView):
    model = RecipeRequirement
    template_name = 'Inventory/requirement.html'

    def get_context_data(self):
        context = super().get_context_data()
        context['requirements'] = RecipeRequirement.objects.all()
        return context

class CreateRequirementView(LoginRequiredMixin, CreateView):
    model = RecipeRequirement
    template_name = 'Inventory/add_requirement.html'
    form_class = RequirementForm
    success_url='/requirements'

class UpdateRequirementView(LoginRequiredMixin, UpdateView):
    model = RecipeRequirement
    template_name = 'Inventory/update_requirement.html'
    form_class = RequirementForm
    success_url='/requirements'

class DeleteRequirementView(LoginRequiredMixin, DeleteView):
    model = RecipeRequirement
    template_name = 'Inventory/delete_requirement.html'
    success_url='/requirements'


class PurchaseView(ListView):
    model = Purchase
    template_name = 'Inventory/purchase.html'

    def get_context_data(self):
        today = today_object()
        context = super().get_context_data() 
        context['purchases'] = Purchase.objects.filter(purchase_day = today)
        context['this_day'] = today
        return context

class CreatePurchaseView(LoginRequiredMixin, CreateView):
    model = Purchase
    template_name = 'Inventory/add_purchase.html'
    form_class = PurchaseForm
    success_url='/purchases'

class UpdatePurchaseView(LoginRequiredMixin, UpdateView):
    model = Purchase
    template_name = 'Inventory/update_purchase.html'
    form_class = PurchaseForm
    success_url='/purchases'

class DeletePurchaseView(LoginRequiredMixin, DeleteView):
    model = Purchase
    template_name = 'Inventory/delete_purchase.html'
    success_url='/purchases'


class PurchasesByDayView(DetailView):
    model = Day
    template_name = 'Inventory/purchases_sort_by_day.html'
    context_object_name = 'day'

class FinishDayView(UpdateView):
    model = Day
    template_name = 'Inventory/finish_day.html'
    form_class = DayForm
    success_url = '/day_summary'
    
    def form_valid(self, form):
        day = form.save(commit = False)
        day.finish_day()
        day.save()
        return super().form_valid(form)
