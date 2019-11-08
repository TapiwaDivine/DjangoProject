from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from .forms import BugCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Bug

def render_contact_us_page(request):
    #this function is for rendering contact_us html file
    return render(request, 'contact_us.html')
    
def display_community_page(request):
    #this function is for displaying commnuty page and rendering 3 bugs on the commuity page
    bug_view = Bug.objects.all().order_by('id')[:3]
    return render(request, 'community.html', {'bugs': bug_view})

@login_required
def bug_form_page(request):
    #this function is for creating an issue and display the bugform page
    if request.method == "POST":
        form = BugCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, "Issue has been Submitted!")
            form.save()
    else:
        form = BugCreationForm() 
    return render(request, 'bugform.html', {"bug_form": form})
    
def render_all_bugs(request):
    # function to display all issues a on single page
    bug_view = Bug.objects.all()
    return render(request, 'display_allbugs.html', {'bugs': bug_view})

def view_bug_details(request, id):
    # function to view one issue in detail on a template
    bug = get_object_or_404(Bug, pk=id)
    return render(request, 'bugview.html', {'bug': bug})  
    
@login_required
def edit_issue(request, id):
    bug = get_object_or_404(Bug, pk=id)
    form = BugCreationForm(request.POST or None)
    if request.user == bug.user:
        if form.is_valid():
            bug = form.save(commit=False)
            bug.save()
    return redirect(reverse(request, 'edit_issue.html', {"bug_form": form}))

@login_required
def delete_issue(request, id):
    bug = get_object_or_404(Bug, id=id)
    try:
        if request.method == "POST":
            if request.user == bug.user:
                delete_form = BugForm(request.POST, instance=bug)
                bug.delete()
                messages.success(request, "Issue has been deleted")
        else:
            delete_form = BugForm(instance=bug)
            
    except Exception as e:
        messages.warning(request, 'Deletion Failed: Error{}")
        
                
    
        
    return redirect(reverse(request, '../'))
    
    
    
    
        
 
        
       
            
            
            