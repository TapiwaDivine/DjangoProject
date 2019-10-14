from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError

class UserLoginForm(forms.Form):
    #This form is used to login in users
    username = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput())


 
class UserRegistrationForm(UserCreationForm):
    #This form is used to register new users
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", 
                                widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'password1', 'password2']
