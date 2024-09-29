from django.db import models
from datetime import datetime

class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=30)
    unit_price = models.FloatField(default=0.0)
    unit = models.CharField(max_length=10)
    quantity = models.FloatField(default = 0.0)

    def __str__(self):
        return self.ingredient_name
    
    def get_absolut_url(self):
        return '/ingredient'


class MenuItem(models.Model):
    item_name = models.CharField(max_length=30)
    price = models.FloatField(default=0.0)
    
    def __str__(self):
        return self.item_name
    
    def get_absolut_url(self):
        return '/menu'


class RecipeRequirement(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete= models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete = models.CASCADE)
    quantity = models.FloatField(default = 0.0)

    def __str__(self):
        return str(self.menu_item)
    
    def get_absolut_url(self):
        return '/requirement'


class Purchase(models.Model):
    customer_name = models.CharField(max_length=30)
    purchase_time = models.DateTimeField(default=datetime.now())
    purchased_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return str(self.purchased_item)
    
    def get_absolut_url(self):
        return '/purchase'
    


