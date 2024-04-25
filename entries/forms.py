from django import forms
from .models import Entry

# Authentication modules start here
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms.widgets import PasswordInput, TextInput

# Form to create a journal entry
class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        exclude = ["trader"]

# Create / register a user
class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = User #default django User model
        fields = ['username', 'email', 'password1', 'password2']


# Authenticate a user
class LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())

