from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.HomeView.as_view(), name='home'),
    path('menu/', views.MenuView.as_view(), name='menu'),
    path('ingredients/', views.IngredientsView.as_view(), name='ingredientlist'),
    path('purchases/', views.PurchaseView.as_view(), name='purchase'),
    path('menu/new', views.CreateMenuItemView.as_view(), name='addmenuitem'),
    path('ingredient/new', views.CreateIngredientView.as_view(),name='addingredient'),
    path('purchases/new', views.CreatePurchaseView.as_view(),name='addpurchase'),
    path('menu/update/<pk>', views.UpdateMenuItemView.as_view(),name='updatemenuitem'),
    path('ingredients/update/<pk>',views.UpdateIngredientView.as_view(),name='updateingredient'),
    path('purchases/update/<pk>',views.UpdatePurchaseView.as_view(),name='updatepurchase'),
    path('menu/delete/<pk>', views.DeleteMenuItemView.as_view(), name='deletemenuitem'),
    path('ingrediets/delete/<pk>', views.DeleteIngredientView.as_view(),name='deleteingredient'),
    path('purchases/delete/<pk>',views.DeletePurchaseView.as_view(),name='deletepurchase'),
    path('day_summary/',views.DaySummaryView.as_view(), name='daysummary'),
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('account/', include('django.contrib.auth.urls'), name='login'),
    path('logout', include('django.contrib.auth.urls'), name='logout'),
    path('accounts/profile/', views.HomeView.as_view(), name='days'),
    path('days/<pk>/purchases/', views.PurchasesByDayView.as_view(), name='purchasesbyday'),
    path('purchases/<pk>/finish_day', views.FinishDayView.as_view(), name='finishday'),
    path('menu/<pk>/recipe',views.RecipeDetailView.as_view(), name='recipe'),
    path('menu/<pk>/recipe/add_ingredient', views.CreateRecipeView.as_view(), name='addrecipe'),
]
