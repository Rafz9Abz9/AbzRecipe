from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.validators import EmailValidator
from django.contrib.auth.models import User

class RegistrationForm(UserCreationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'User name',
        'class': 'form-control input-lg'
        }), required=True)
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={
            'placeholder': 'Email Address',
            'class': 'form-control input-lg'
        }), required=True)
    
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control input-lg'
        }),
        required=True,
        min_length=8 
    )

    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Confirm Password',
            'class': 'form-control input-lg'
        }),
        required=True
    )
        
    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 != password2:
            self.add_error('password2', "Passwords do not match.")

        email = cleaned_data.get('email')
        email_validator = EmailValidator(message="Enter a valid email address.")
        
        try:
            email_validator(email)
        except forms.ValidationError as e:
            self.add_error('email', e)
            
    
    class Meta:
        model = User
        fields = ('username', 'email',  'password1', 'password2' )



class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'form-control input-lg',
    }), required=True)
    
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'Password',
            'class': 'form-control input-lg',
        }),
        required=True,
    )