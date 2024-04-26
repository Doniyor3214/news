from django import forms
from django.contrib.auth.models import User
  
from .models import News, Category, Comment, User


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']

class PasswordForm(forms.Form):
     password_1 = forms.CharField(max_length=50)
     password_2 = forms.CharField(max_length=60)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password', 'email']

class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'text', 'rasm', 'tur']

        def __init__(self, *a, **b): 
            pass

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['izoh']  

class LoginForm(forms.Form):
        username = forms.CharField(max_length=50)
        password = forms.CharField(max_length=60)
