from django.db import models

# Create your models here.

class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Recipe(models.Model):
    name = models.CharField(max_length=8191)
    image_url = models.URLField()

class RecipeInfo(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=8191)
    description = models.TextField()
    cuisine = models.CharField(max_length=8191)
    course = models.CharField(max_length=8191)
    diet = models.CharField(max_length=8191)
    ingredients_name = models.CharField(max_length=8191)
    ingredients_quantity = models.CharField(max_length=8191)
    prep_time = models.IntegerField()
    cook_time = models.IntegerField()
    instructions = models.TextField()
    image_url = models.URLField()
    rating = models.FloatField()

    def __str__(self):
        return self.name
