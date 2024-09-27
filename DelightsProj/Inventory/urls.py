from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('Inventory/menu.html', views.MenuView.as_view(), name='menu'),
    path('Inventory/ingredient_list.html', views.IngredientsView.as_view(), name='ingredientlist'),
    path('Inventory/requirement.html', views.RequirementView.as_view(), name='requirement'),
    path('Inventory/purchase.html', views.PurchaseView.as_view(), name='purchase'),
]
