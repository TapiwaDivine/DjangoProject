from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from home import views
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm
from django.contrib.auth.models import User
from .models import Profile
from accounts.forms import UserLoginForm, UserRegistrationForm

@login_required
def logout(request):
    # For logging users out
    auth.logout(request)
    messages.success(request, "You have been succcesfully logged out")
    return redirect(reverse('index'))

def login(request):
    # return login page and login functionality
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You're succefully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
    
def registration(request):
    # return signup page
    if request.user.is_authenticated:
        return redirect(reverse('index'))
        
    if request.method == "POST":
        registartion_form = UserRegistrationForm(request.POST)
        
        if registartion_form.is_valid():
            registartion_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have succefully been registered")
                return redirect(reverse('index'))
    
            else:
                messages.error(request, " Unable to register your account at this time")
    else:
        registartion_form = UserRegistrationForm()
    return render(request, "signup.html", {"signup_form": registartion_form})
    
@login_required
def user_profile(request):
    #Profile page for users
    user = User.objects.get(email=request.user.email)
    return render(request, "profile.html", {"profile": user})
