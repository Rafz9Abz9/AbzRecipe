from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
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


def index(request):
    return render(request, 'index.html')


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
            #path to view
            # - get app domain
            # - relative url
            # encode uuid
            # get token
            token = token_generator.make_token(user)
            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            link = reverse('activate', kwargs={
                'uidb64': uidb64, 'token': token
            })
            
            domain = get_current_site(request).domain
            activate_url = 'http://'+domain+link
            email_body = "Hi " + user.username+ " Please use this link to veify your account\n"+activate_url
            
            email = EmailMessage(
                email_subject,
                email_body,
                "noreply@abzrecipe.com",
                [user.email],
                headers={"Message-ID": "abzrecipe"},
            )
            email.send(fail_silently=False)
            
            messages.success(request, "Registration Successfull, check your mail box for activation mail to activate your account")

            return redirect('login')
    else:
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
            return redirect('home')
        else:
            messages.error(request, "Invalid Credentials")
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})


class VerifivationView(View):
    def get(self, request, uidb64, token):
        try:
            id = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)
            
            if user.is_active:
                messages.info(request, "user account is alreeady acivated.")
                login(request,user)
                # Redirect to a success page, e.g., user's profile page
                greetings = "You're Welcome "+user.username
                messages.success(request, greetings)
                return redirect("home")
            user.is_active = True
            user.save()
            messages.success(request, "Account Activated Successfully.")
            return redirect("login")
            
        except Exception as ex:
            messages.error(request, "Error Activating Your Account.")
        return redirect("login")
    
    
