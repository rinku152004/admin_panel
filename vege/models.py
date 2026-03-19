from django.db import models

# Create your models here.
class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_ingredients = models.TextField()
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/')

    def __str__(self):
        return self.recipe_name