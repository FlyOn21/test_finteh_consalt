from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from django import forms
from django.forms import Form

from .models import User,Posts,PostComments

class LoginForm(AuthenticationForm):
    email = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("email", "password")

class RegistrationForm(UserCreationForm):
    email = forms.CharField(widget=forms.TextInput())
    password1 = forms.CharField(widget=forms.PasswordInput())
    password2 = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = (
            "email",
            "password1",
            "password2",
        )

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["post_title","post_text","photo","owner_user" ]

class CommentsForm(forms.ModelForm):
    class Meta:
        model = PostComments
        fields = ["comment_text", "post_id"]

class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = ["post_title","post_text","photo" ]