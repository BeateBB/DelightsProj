from django.db import models
from datetime import datetime
from django.core.exceptions import ValidationError



class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    cost = models.FloatField(default=0.0)
    revenue = models.FloatField(default=0.0)

    def calc_revenue(self):
        self.revenue = self.price - self.cost
        self.save()
    
    def __str__(self):
        return self.item_name
    
    def get_absolute_url(self):
        return '/menu'    

    
class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10)
    quantity = models.FloatField(default = 0.0)

    def __str__(self):
        return self.ingredient_name
    
    def get_absolute_url(self):
        return '/ingredient'
    


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
    

    def __str__(self):
        return str(self.purchased_item)
    
    def get_absolute_url(self):
        return '/purchase'
    
    def clean(self):
        recipe_reqs = RecipeRequirement.objects.filter(menu_item = self.purchased_item)
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
        day = Day.objects.get_or_create(date = datetime.today())
        day.purchases.add(self)


        
        
        if not DaySummary.objects.first():
            DaySummary.objects.create()
        day_summary = DaySummary.objects.first()
        day_summary.num_purchases+=1
        cost = self.purchased_item.cost
        day_summary.total_cost+=cost
        revenue = self.purchased_item.price - self.purchased_item.cost
        day_summary.total_revenue +=revenue        
        day_summary.save()
        super(Purchase,self).save()
    
    
    
class DaySummary(models.Model):
    num_purchases = models.FloatField(default=0.0)
    total_cost = models.FloatField(default=0.0)
    total_revenue = models.FloatField(default=0.0)



class Day(models.Model):
    date = models.DateField(auto_now_add=True)
    purchases = models.ManyToManyField(Purchase)
    inventory = models.ManyToManyField(Ingredient)
    summary = models.ForeignKey(DaySummary,on_delete=models.CASCADE)
