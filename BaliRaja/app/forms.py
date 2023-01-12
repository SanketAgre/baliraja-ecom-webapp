from dataclasses import field
from django.contrib.auth.forms import UserCreationForm

from .models import User
from django import forms

class costomuserform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my2','placeholder':'Enter Username'}))
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my2','placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2','placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my2','placeholder':'Enter Password'}))

    class Meta:
        model=User
        fields=['username','email','password1','password2']
