from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):
    title = models.TextField(max_length=10, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def count_recipes_by_category(self):
        recipe_count = RecipeCategory.objects.filter(category__title=self.title).count()
        
        return recipe_count

    def __str__(self):
        return f"{self.title}"
    
    

class Recipe(models.Model):
    title = models.TextField(max_length=100, blank=True)
    description = models.TextField(max_length=500, blank=True)
    created_by = models.ForeignKey(User,  on_delete=models.SET_NULL, null=True)
    image = CloudinaryField('recipe_images', null=True, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    special = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title}"


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.recipe}  belongs {self.category} category"

class RecipeStep(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    title = models.TextField(max_length=250, blank=True)
    content = models.TextField(max_length=800)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.title} >> {self.recipe.title}"
    
class Ingredient(models.Model):
    title = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.title}"

class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.ingredient.title} for {self.recipe.title}"

class FavoriteRecipe(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f" {self.user.username} favrecipe>> {self.recipe.title}"
    
class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    message = models.CharField(max_length=1050)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return f"Comment by {self.name} for  {self.recipe.title}"
    
    

    

    

