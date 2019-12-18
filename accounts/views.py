from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from home import views
from django.contrib.auth.decorators import login_required
from accounts.forms import UserLoginForm
from django.contrib.auth.models import User
from .models import Profile
from accounts.forms import UserLoginForm, UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from issue_tracker.models import Bug
from services.models import Feature

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
            user = auth.authenticate(request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(request, user)
                request.session["user"] = user.id
                messages.success(request, "You're succefully logged in!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Your username or password is incorrect!")
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()
    return render(request, "login.html", {"login_form": login_form})
    
def registration(request):
    # this function is for registering users
    if request.user.is_authenticated:
        return redirect(reverse('profile'))
        
    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)
        
        if registration_form.is_valid():
            registration_form.save()
            
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])
            
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully been registered")
                return redirect(reverse('profile'))
    
            else:
                messages.error(request, " Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()
    return render(request, "signup.html", {"signup_form": registration_form})
    
@login_required
def user_profile(request):
    user_info = Profile.objects.get(user=request.user)
    logged_in_user_bug = Bug.objects.filter(author=request.user)
    logged_in_user_feature = Feature.objects.filter(author=request.user)
    context = {
        "user_info": user_info,
        "user_bug": logged_in_user_bug,
        "user_feature": logged_in_user_feature
    }
    return render(request, "profile.html", context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, 
                                   request.FILES,
                                   instance=request.user.profile)
                                   
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your Profile has been updated')
            return redirect('profile')
            
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "edit_profile.html", context)