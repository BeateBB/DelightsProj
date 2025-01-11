from typing import Any, Iterable
from django.db import models
from datetime import datetime, date
from django.core.exceptions import ValidationError


class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    cost = models.FloatField(default=0.0)
    revenue = models.FloatField(default=0.0)

    def calc_revenue(self):
        self.revenue = round(self.price - self.cost,1)
           
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return '/menu'

    def save(self):
        self.calc_revenue()
        super(MenuItem,self).save()    

    
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10)
# available amount of the ingredient
    quantity = models.FloatField(default = 0.0)
# required amount of the ingredient to be available in the morning
    start_quantity = models.FloatField(default=0.0)
    quantity_to_purchase = models.FloatField(default=0.0)

    def purchase_ingredient(self):
        if self.quantity < self.start_quantity:
            self.quantity_to_purchase = self.start_quantity - self.quantity

    def __str__(self):
        return self.ingredient_name
    
    def get_absolute_url(self):
        return '/ingredient'
    
    def save(self):
        self.purchase_ingredient()
        super(Ingredient,self).save()



class RecipeRequirement(models.Model):
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField(default = 0.0)

    def __str__(self):
        return str(self.menu_item)
    
    def get_absolute_url(self):
        return '/requirement'
    
    def save(self):
        cost = self.ingredient.unit_price * self.quantity
        self.menu_item.cost+=cost
        self.menu_item.revenue = self.menu_item.price - self.menu_item.cost
        self.menu_item.save()
        super(RecipeRequirement,self).save()

    def delete(self):
        cost = self.ingredient.unit_price * self.quantity
        self.menu_item.cost-=cost
        self.menu_item.save()
        super(RecipeRequirement,self).delete()
    
class Purchase(models.Model):
    customer_name = models.CharField(max_length=30)
    purchase_time = models.DateTimeField(default=datetime.now())
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    purchase_day = models.ForeignKey("Day", on_delete=models.CASCADE, null=True)
    
    def get_ingredients(self):
        recipe_reqs = RecipeRequirement.objects.filter(menu_item = self.purchased_item)
        return recipe_reqs
        

    def __str__(self):
        return str(self.purchased_item)
    
    def get_absolute_url(self):
        return '/purchase'
    
    
    def clean(self):
        recipe_reqs = self.get_ingredients()
        for recipe_req in recipe_reqs:
            ingredient = recipe_req.ingredient
            required_quantity = recipe_req.quantity*self.quantity
            if ingredient.quantity < required_quantity:
                raise ValidationError(f'Not enough quantity of {ingredient} to make this dish')
            else:
                ingredient.quantity -= required_quantity
                ingredient.save()
        return super().clean()

    def save(self):
        self.purchase_day = Day.objects.get(date = date.today())
        self.purchase_day.num_purchases+=1
        cost = self.purchased_item.cost
        self.purchase_day.total_cost+=cost
        revenue = self.purchased_item.price - self.purchased_item.cost
        self.purchase_day.total_revenue +=revenue        
        self.purchase_day.save()
        super(Purchase,self).save()

    def delete(self):
        recipe_reqs = RecipeRequirement.objects.filter(menu_item = self.purchased_item)
        for recipe in recipe_reqs:
            ingredient=recipe.ingredient
            ingredient.quantity += recipe.quantity
            ingredient.save()
        return super().delete()


class Day(models.Model):
    date = models.DateField(auto_now_add=True, unique=True)
    is_open = models.BooleanField(default=True)
    today_ingredients = models.ManyToManyField(Ingredient)
    num_purchases = models.FloatField(default=0.0)
    total_cost = models.FloatField(default=0.0)
    total_revenue = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.date)
    
    def finish_day(self):
        self.is_open = False
        self.save()
 
    def save(self, *args, **kwargs):
        yesterday = Day.objects.order_by('-pk')[0]
        yesterday_ingredients = yesterday.today_ingredients.all()
        super(Day,self).save(*args,**kwargs)
        for ingredient in yesterday_ingredients:
            self.today_ingredients.add(ingredient)
        

