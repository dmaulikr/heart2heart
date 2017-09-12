from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms

class MyAuthenticationForm(AuthenticationForm):
    """ Authenticationform superclass for customized form labels """
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'input-md form-control"'}))
    password = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class':'input-md form-control"'}))
    
    class Meta:
        fields = ('username', 'password')

class SignupForm(UserCreationForm):
    email = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=30, required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput(attrs={'class':'form-control'}))

    class Meta:
        model = User
        fields = ("email", "username", "password1", "password2")

