from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from .models import Task

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
  

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']
        labels = {
            'title' : 'Title',
            'description' : 'Description',
        }

        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'description' : forms.Textarea(attrs={'class': 'form-control'}),
        }