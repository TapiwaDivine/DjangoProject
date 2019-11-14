from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import FeatureCreationForm
from django.contrib import messages
from .models import Feature

def get_services_page(request):
    # display services page and render features requested on Services page
    feature_view = Feature.objects.all().order_by('date_created')[:3]
    return render(request, "services.html", {'features': feature_view})

def render_all_features(request):
    # function to display all features a on single page
    feature_view = Feature.objects.all()
    return render(request, 'display_allfeatures.html', {'features': feature_view})

def view_feature_details(request, id):
    # function to view one features in detail on a template
    feature = get_object_or_404(Feature, pk=id)
    return render(request, 'featureview.html', {'feature': feature }) 

@login_required
def create_feature_page(request):
    #this function is for creating features and display the create features form page
    if request.method == "POST":
        form = FeatureCreationForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            messages.success(request, "Your Feature request has been Submitted!")
            form.save()
            return redirect(reverse('allfeatures'))
    else:
        form = FeatureCreationForm() 
    return render(request, 'create_feature.html', {"f_form": form})