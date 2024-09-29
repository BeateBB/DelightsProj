from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredientlist'),
    path('requirements/', views.RequirementView.as_view(), name='requirement'),
    path('purchases/', views.PurchaseView.as_view(), name='purchase'),
    path('menu/new', views.CreateMenuItemView.as_view(), name='addmenuitem'),
    path('ingredient/new', views.CreateIngredientView.as_view(),name='addingredient'),
    path('requirements/new', views.CreateRequirementView.as_view(),name='addrequirement'),
    path('purchases/new', views.CreatePurchaseView.as_view(),name='addpurchase'),
    path('menu/update/<pk>', views.UpdateMenuItemView.as_view(),name='updatemenuitem'),
    path('ingredients/update/<pk>',views.UpdateIngredientView.as_view(),name='updateingredient'),
    path('requirements/update/<pk>', views.UpdateRequirementView.as_view(),name='updaterequirement'),
    path('purchases/update/<pk>',views.UpdatePurchaseView.as_view(),name='updatepurchase'),
    path('menu/delete/<pk>', views.DeleteMenuItemView.as_view(), name='deletemenuitem'),
    path('ingrediets/delete/<pk>', views.DeleteIngredientView.as_view(),name='deleteingredient'),
    path('requirements/delete/<pk>',views.DeleteRequirementView.as_view(),name='deleterequirement'),
    path('purchases/delete/<pk>',views.DeletePurchaseView.as_view(),name='deletepurchase'),
]
