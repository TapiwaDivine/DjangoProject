from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import Profile

class UserLoginForm(forms.Form):
    #This form is used to login in users
    username = forms.CharField(max_length=35)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(label="Remember Me", required=False, widget=forms.CheckboxInput())
    

class UserRegistrationForm(UserCreationForm):
    #This form is used to register new users
    password1 = forms.CharField(label="Password",
                                widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password Confirmation", 
                                widget=forms.PasswordInput)
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email' ,'password1', 'password2']
        
    def clean_email(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        if User.objects.filter(email=email).exclude(username=username):
            raise forms.ValidationError(u'Email address must be unique')
        return email
    
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        
        if not password1 or not password2:
            raise ValidationError("Please confirm your password")
        
        if password1 != password2:
            raise ValidationError("Passwords must match")
            
        return password2
        
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name','email']
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['age', 'image', 'location','gender','bio']