from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):

    name = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter your name',
        'class': 'form-control input-lg'
    }), required=True)

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email address',
        'class': 'form-control input-lg'
    }), required=True)

    message = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Enter Message',
        'class': 'form-control input-lg'
    }), required=True)

    class Meta:
        model = Comment
        fields = ('name', 'email', 'message')
