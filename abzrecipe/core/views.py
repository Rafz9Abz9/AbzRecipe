from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm, ProfileUpdateForm, ContactForm
from .models import Profile
# from django.utils import timezone
import json
from django.http import JsonResponse
from django.contrib.auth.models import User
from validate_email import validate_email
from django.contrib.auth import login, logout

from django.core.mail import EmailMessage
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import token_generator

from django.views.generic.base import View
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from recipe.models import Recipe, Category, RecipeCategory
from random import shuffle
from recipe.models import Comment
from collections import defaultdict
from django.db.models import Count
from django.template.defaulttags import register


...
@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


def index(request):
    if request.POST:
        pass
    
    best_recipes = Recipe.objects.filter(special=True).order_by('-created_at') 
    recipes = Recipe.objects.all().order_by('-created_at') 
    other_recipes = Recipe.objects.filter(special=False).order_by('-created_at') 
    shuffled_recipes = list(recipes)
    shuffled_best_recipes = list(best_recipes)
    shuffle(shuffled_recipes)
    shuffle(shuffled_best_recipes)

        # Get all comments
    comments = Comment.objects.all()
    # Get comment counts for each recipe
    comment_counts = Comment.objects.values('recipe').annotate(count=Count('recipe'))
    comment_count_dict = {item['recipe']: item['count'] for item in comment_counts}

    return render(request, 'index.html', {
        'limited_best_recipe': shuffled_best_recipes[:6],
        'other_recipes': other_recipes[:9],
        'limited_recipes': shuffled_recipes[:2],
        'comment_counts': comment_count_dict
    })


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Form data is valid; create a new user,
            user = form.save()
            # create user profile
            new_profile = Profile.objects.create(user=user, id_user=user.id)
            new_profile.save()
            
            user.is_active = False
            user.save()
            # email subject here
            email_subject = 'Activate Your Account'
            # email body
           
            token = token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            link = reverse('activate', kwargs={
                'uidb64': uidb64, 'token': token
            })
            
            domain = get_current_site(request).domain
            activate_url = 'http://'+domain+link
            email_body = "Hi " + user.username+ " Please use this link to veify your account\n"+activate_url
            try:
                # setup email
                email = EmailMessage(
                    email_subject,
                    email_body,
                    "noreply@abzrecipe.com",
                    [user.email],
                    headers={"Message-ID": "abzrecipe"},
                )
                # send email
                email.send(fail_silently=False)
                
                messages.success(request, "Registration Successful, check your mailbox to activate your accouint before login")
                return redirect('login')
            except Exception as e:
                print(f"Error sending email: {e}")
                

    
    form = RegistrationForm()

    return render(request, 'auth/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, "You've been logged out successfully")
    # Redirect to login
    return redirect('login')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            greetings = "You're Welcome "+user.username
            messages.success(request, greetings)
            # redirect to home
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    
    form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


def about(request):
    if request.method == 'POST':
        pass
    all_recipe_count = len(Recipe.objects.all())
    breakfast_recipe_count = RecipeCategory.objects.filter(category__title='breakfast').count()
    dessert_recipe_count = RecipeCategory.objects.filter(category__title='dessert').count()
    lunch_recipe_count = RecipeCategory.objects.filter(category__title='lunch').count()
    dinner_recipe_count = RecipeCategory.objects.filter(category__title='dinner').count()
    beverages_recipe_count = RecipeCategory.objects.filter(category__title='beverages').count()
    snacks_recipe_count = RecipeCategory.objects.filter(category__title='snacks').count()
    soups_recipe_count = RecipeCategory.objects.filter(category__title='soups').count()
    salads_recipe_count = RecipeCategory.objects.filter(category__title='salads').count()

    return render(request, 'about/about.html',
        {
        'all_recipe_count': all_recipe_count,
        'breakfast_recipe_count': breakfast_recipe_count,
        'dessert_recipe_count': salads_recipe_count,
        'lunch_recipe_count': lunch_recipe_count,
        'dinner_recipe_count': dinner_recipe_count,
        'beverages_recipe_count': beverages_recipe_count,
        'snacks_recipe_count': snacks_recipe_count,
        'soups_recipe_count': soups_recipe_count,
        'salads_recipe_count': salads_recipe_count
    })


def contact(request):
    if request.method == 'POST':
       contact_form = ContactForm(request.POST)

       if contact_form.is_valid():

        contact = contact_form.save()

        email_subject = '@abzrecipehotdesk'
        email_msg = " Your message has been submitted. We'll get in touch with you soon."       
        email_body = "Hi " + contact.name + email_msg
        try:
                     # setup email
            email = EmailMessage(
                    email_subject,
                    email_body,
                    "noreply@abzrecipe.com",
                    [contact.email],
                    headers={"Message-ID": "abzrecipe"},
                )
                # send email
            email.send(fail_silently=False)
            messages.success(request, "Comment submitted successfully")
            return redirect('contact')
        except Exception as e:
            print(f"Error sending email: {e}")
       
       else:
        messages.error(request, "Invalid Form")

    contact_form = ContactForm()

    return render(request, 'contact/contact.html',
        {
            'contact_form': contact_form,
        })


@login_required(login_url='login')
def update_profile_view(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()  # Save the User model
            profile, created = Profile.objects.get_or_create(user=user)
            profile.address = form.cleaned_data['address']
            profile.phone = form.cleaned_data['phone']
            profile.country = form.cleaned_data['country']
            profile.save()
            messages.success(request, 'Profile updated successfully')
            # redirect to profile
            return redirect('profile') 
        else:
            messages.error(request, "Error  in Completing profile update")

    form = ProfileUpdateForm()
    
    if request.user.is_authenticated:
        user = request.user
        profile, created = Profile.objects.get_or_create(user=user)
        initial_data = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username,
            'email': user.email,
            'address': profile.address,
            'phone': profile.phone,
            'country': profile.country,
        }
        form = ProfileUpdateForm(instance=user, initial=initial_data)
    else:
        messages.error(request, "Login is required")
        return redirect('login')

    return render(request, 'profile/profile.html', {'form': form})




class VerifivationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            greetings = "You're Welcome "+user.username + "Account activated successfully."
            if user.is_active:
                messages.info(request, "user account is alreeady acivated.")
                login(request,user)
                # Redirect to a success page, e.g., user's profile page
                messages.success(request, greetings)
                return redirect("home")
            user.is_active = True
            user.save()
            login(request,user)
            messages.success(request, greetings)
            return redirect("home")
            
        except Exception as ex:
            messages.error(request, "Error Activating Your Account.")
        return redirect("login")
    
    
