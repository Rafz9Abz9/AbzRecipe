from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Recipe, Category, RecipeCategory
from .models import RecipeIngredient, RecipeStep, Comment, FavoriteRecipe
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.http import HttpResponseRedirect


def recipes(request):
    if request.method == 'POST':
        pass

    all_recipe = Recipe.objects.all().order_by('-created_at')
    categories = Category.objects.all()

    category = request.GET.get('category')

    if category:
        recipe_ids = RecipeCategory.objects.filter(
            category=category).values_list('recipe_id', flat=True)
        all_recipe = Recipe.objects.filter(id__in=recipe_ids)

    paginator = Paginator(all_recipe, 8)
    page = request.GET.get('page')

    try:
        recipes = paginator.page(page)
    except PageNotAnInteger:
        recipes = paginator.page(1)
    except EmptyPage:
        recipes = paginator.page(paginator.num_pages)

    return render(request, 'recipes/recipes.html', {
        'recipes': recipes,
        'categories': categories,
        'category': category
    })


def recipe_detail(request, recipe_id):
    
    comment_form = CommentForm()

    if request.user.is_authenticated:
        user = request.user
        initial_data = {
            'name': user.username,
            'email': user.email,
        }
        comment_form = CommentForm(instance=user, initial=initial_data)

    categories = Category.objects.all()
    recipe = get_object_or_404(Recipe, pk=recipe_id)
    ingredients = RecipeIngredient.objects.filter(recipe=recipe)
    steps = RecipeStep.objects.filter(recipe=recipe)
    recipe_categories = RecipeCategory.objects.filter(recipe=recipe)
    related_recipes = Recipe.objects.filter(
        recipecategory__category__in=recipe_categories.values_list(
            'category', flat=True)
    ).exclude(pk=recipe_id).distinct()

    comments = Comment.objects.filter(recipe=recipe)
    recipe_favorite_list = FavoriteRecipe.objects.filter(recipe=recipe)
    like_by_user = ''

    if request.user.is_authenticated:
        like_by_user = FavoriteRecipe.objects.filter(
            user=request.user, recipe=recipe)

    return render(request, 'recipe/recipe.html', {
        'comment_form': comment_form,
        'recipe': recipe,
        'categories': categories,
        'ingredients': ingredients,
        'steps': steps,
        'related_recipes': related_recipes,
        'comments': comments,
        'recipe_favorite_list': recipe_favorite_list,
        'like_by_user': like_by_user
    })
    
    

def comment_to_recipe(request, recipe_id):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if request.user.is_authenticated:
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                recipe = get_object_or_404(Recipe, pk=recipe_id)
                comment.recipe = recipe
                comment.save()

                email_subject = '@abzrecipehotdesk'
                email_msg = " Your comment has been submitted."
                email_body = "Hi " + comment.name + email_msg

                try:
                    email = EmailMessage(
                        email_subject,
                        email_body,
                        "noreply@abzrecipe.com",
                        [comment.email],
                        headers={"Message-ID": "abzrecipe"},
                    )
                    email.send(fail_silently=False)
                    messages.success(request, "Comment submitted successfully")
                    return redirect('recipe_detail', recipe_id=recipe_id)
                except Exception as e:
                    print(f"Error sending email: {e}")
            else:
                messages.error(request, "Invalid form")
        else:
            messages.warning(request, 'Only authenticated user is allowed to add comment')
        
    comment_form = CommentForm()

    if request.user.is_authenticated:
        user = request.user
        initial_data = {
            'name': user.username,
            'email': user.email,
        }
        comment_form = CommentForm(instance=user, initial=initial_data)

    return render(request, 'recipe/recipe.html', {'comment_form':comment_form})


def user_comments(request):
    comments = None
    if request.user.is_authenticated:
        comments = Comment.objects.filter(email=request.user.email)
    else:
        messages.warning(request, 'Only Authenticated user is allow to access this page')
        return redirect('login')
    return render(request, 'comments/comments.html', {'comments': comments})

def update_comment(request, comment_id):
    if request.method == 'POST':
        if request.user.is_authenticated:
            comment = get_object_or_404(Comment, pk=comment_id)
            
            comment.name = request.POST.get('name')
            comment.message = request.POST.get('message')
            comment.save()
            messages.success(request, f'Comment on {comment.recipe.title} updated successfully')
        else:
            messages.warning(request, 'Only authenticated user is allowed to add comment')
    return render(request, 'recipe/recipe.html')


def delete_comment(request, recipe_id, comment_id):
    if request.method == 'POST':
        pass
    else:
        if request.user.is_authenticated:
            user = request.user
            comment = get_object_or_404(Comment, pk=comment_id)
            if comment and comment.name == user.username:
                comment.delete()
                messages.success(request, 'Comment deleted successfully')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                messages.error(request, 'Comment not found')
        else:
            messages.error(request, "Login is required")
            return redirect('login')

    return redirect('recipe_detail', recipe_id=recipe_id)


def like_recipe(request, recipe_id):
    if request.method == 'POST':
        pass

    if request.user.is_authenticated:
        recipe = get_object_or_404(Recipe, pk=recipe_id)
        is_liked_by_user = FavoriteRecipe.objects.filter(
            recipe=recipe,
            user=request.user
        )
        if is_liked_by_user:
            is_liked_by_user.delete()
            messages.success(request, 'Recipe removed from favorites.')
        else:
            FavoriteRecipe.objects.create(recipe=recipe, user=request.user)
            messages.success(request, 'Recipe added to favorites.')
    else:
        messages.error(request, "Login is required")
        return redirect('login')

    return redirect('recipe_detail', recipe_id=recipe_id)


def favorite_recipe(request):
    if request.method == 'POST':
        pass

    if request.user.is_authenticated:
        all_favorite_recipes = FavoriteRecipe.objects.filter(user=request.user)

        paginator = Paginator(all_favorite_recipes, 8)
        page = request.GET.get('page')

        try:
            favorite_recipes = paginator.page(page)
        except PageNotAnInteger:
            favorite_recipes = paginator.page(1)
        except EmptyPage:
            favorite_recipes = paginator.page(paginator.num_pages)
    else:
        messages.error(request, "Login is required")
        return redirect('login')

    return render(request, 'favorite/favorite.html', {
        'favorite_recipes': favorite_recipes
    })
