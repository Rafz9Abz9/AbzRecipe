from django.contrib import admin
from .models import Category, Recipe, RecipeStep, Ingredient, RecipeIngredient, FavoriteRecipe, RecipeCategory, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(RecipeStep)
admin.site.register(Ingredient)
admin.site.register(RecipeIngredient)
admin.site.register(FavoriteRecipe)
admin.site.register(RecipeCategory)
admin.site.register(Comment)
