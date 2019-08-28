from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from home import views

def logout(request):
    # For logging users out
    auth.logout(request)
    messages.success(request, "You have been succcesfully logged out")
    return redirect(reverse('index'))
    
def login(request):
    # return login page
    return render(request, "login.html")
    
def signup(request):
    # return signup page
    return render(request, "signup.html")
    
