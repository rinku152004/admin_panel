from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Recipe(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_ingredients = models.TextField()
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to='recipes/')
    
    recipe_views_count = models.IntegerField(default=1)

    def __str__(self):
        return self.recipe_name