from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Recipe, Category, RecipeCategory, RecipeIngredient, RecipeStep, Comment, FavoriteRecipe
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def recipes(request):
    if request.method == 'POST':
        pass
    else:
        all_recipe = Recipe.objects.all().order_by('-created_at') 
        categories = Category.objects.all()

        category= request.GET.get('category')

        if category:
            recipe_ids = RecipeCategory.objects.filter(category=category).values_list('recipe_id', flat=True)
            
            all_recipe = Recipe.objects.filter(id__in=recipe_ids)

        paginator = Paginator(all_recipe, 8)
        page = request.GET.get('page')

        try:
            recipes = paginator.page(page)
        except PageNotAnInteger:
            recipes = paginator.page(1)

        except EmptyPage:
            recipes = paginator.page(paginator.num_pages)
    return render(request, 'recipes/recipes.html', {'recipes':recipes, 'categories':categories,  'category': category})


def recipe_detail(request, recipe_id):
    if request.method == 'POST':
    #    save comment
       comment_form = CommentForm(request.POST)
       comment_form = CommentForm(request.POST)
       if comment_form.is_valid():
            # Set the recipe for the comment before saving
            comment = comment_form.save(commit=False)
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            comment.recipe = recipe
            comment.save()
            messages.success(request, "Thanks for you comment, We'll get in touch with you soon")
            return redirect('recipe_detail', recipe_id=recipe_id)
       else:
           messages.error(request, "Something went wrongn")
    else:
        comment_form = CommentForm()
        categories = Category.objects.all()
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        #Get all recupe ingrdient
        ingredients = RecipeIngredient.objects.filter(recipe=recipe)
        # Get all recipe steps
        steps =RecipeStep.objects.filter(recipe=recipe)
        # Get the categories associated with the current recipe
        recipe_categories = RecipeCategory.objects.filter(recipe=recipe)
        # Get other recipes with the same category
        related_recipes = Recipe.objects.filter(
            recipecategory__category__in=recipe_categories.values_list('category', flat=True)
        ).exclude(pk=recipe_id).distinct()

        # Get all comments
        comments = Comment.objects.filter(recipe=recipe)
        recipe_favorite_list = FavoriteRecipe.objects.filter(recipe=recipe)
        like_by_user = FavoriteRecipe.objects.filter(user=request.user, recipe=recipe)

        

    return render(request, 'recipe/recipe.html', {
        'comment_form': comment_form,
        'recipe':recipe, 
        'categories':categories, 
        'ingredients': ingredients,
        'steps': steps,
        'related_recipes': related_recipes,
        'comments':comments,
        'recipe_favorite_list': recipe_favorite_list,
        'like_by_user': like_by_user
        })

login_required
def like_recipe(request, recipe_id):
    if request.method == 'POST':
        pass
    else:
        # Check if the user is authenticated
        if request.user.is_authenticated:
            recipe = get_object_or_404(Recipe, pk=recipe_id)
            is_liked_by_user =FavoriteRecipe.objects.filter(recipe=recipe, user=request.user)
            if is_liked_by_user:
                # If liked, unlike the recipe
                is_liked_by_user.delete()
                messages.success(request, 'Recipe removed from favorites.')
            else:
                FavoriteRecipe.objects.create(recipe=recipe, user=request.user)
                messages.success(request, 'Recipe added to favorites.')
        else:
            messages.error(request, "Login is required")
            return redirect('login')

    return redirect('recipe_detail', recipe_id=recipe_id)
        
        
