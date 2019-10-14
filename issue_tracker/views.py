from django.shortcuts import render, redirect, reverse
from django.http import HttpResponseRedirect
from .forms import BugCreationForm
from django.contrib import messages
from .models import Bug

def render_contact_us_page(request):
    #this function is for rendering contact_us html file
    return render(request, 'contact_us.html')
    
def display_community_page(request):
    #this function is for displaying commnuty page
    bug_view = Bug.objects.all().order_by('id')[:3]
    return render(request, 'community.html', {'bugs': bug_view})
    
def bug_form_page(request):
    #this function is for creating bugform and display the bugform page
    if request.method == "POST":
        form = BugCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Your Issue has been Submitted!")
            form.save()
    else:
        form = BugCreationForm() 
    return render(request, 'bugform.html', {"bug_form": form})
    
def view_bug_details(request, *args, **kwargs):
    bug = Bug.objects.get().filter(id)['']
    print(bug)
    return render(request, 'bugview.html', {'bug': bug})
    
def render_all_bugs(request):
    bug_view = Bug.objects.all()
    return render(request, 'display_allbugs.html', {'bugs': bug_view})
    
    
        
 
        
       
            
            
            