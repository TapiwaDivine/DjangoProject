from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import FeatureCreationForm, CommentForm
from django.contrib import messages
from .models import Feature
from accounts.models import Profile

def get_services_page(request):
    # display services page and render features requested on Services page
    feature_view = Feature.objects.all().order_by('date_created')[:3]
    return render(request, "services.html", {'features': feature_view})

def render_all_features(request):
    # function to display all features a on single page
    feature_view = Feature.objects.all()
    return render(request, 'display_allfeatures.html', {'features': feature_view})
    
@login_required
def view_feature_details(request, id):
    # function to view one features in detail on a template
    feature = get_object_or_404(Feature, pk=id)
    is_liked = False
    # this function also creates a comments form on the page
    if request.method == 'POST':
         form = CommentForm(request.POST)
         if form.is_valid():
             print(form)
             form.instance.author = request.user
             comment = form.save(commit=False)
             comment.feature = feature
             comment.save()
             return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = CommentForm()

    if feature.votes.filter(id=request.user.id).exists():
        is_liked
    else:
        is_liked = True
        
    context = {
        'feature': feature,
        'c_form': form,
        'is_liked': is_liked,
        }
    return render(request, 'featureview.html', context) 


def like_a_feature_post(request):
    feature = get_object_or_404(Feature, id=request.POST.get('feature_id'))
    is_liked = False
    if feature.votes.filter(id=request.user.id).exists():
        feature.votes.remove(request.user)
        is_liked
    else:
        feature.votes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(feature.get_absolute_url())
    
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
    
@login_required
def edit_feature(request, id):
    feature = get_object_or_404(Feature, pk=id)
    if request.method == 'POST':
        if request.user == feature.author:
            form = FeatureCreationForm(request.POST, instance=feature)
            try:
                if form.is_valid():
                    form.save()
                    messages.success(request, 'Feature has been updated')
                    return redirect('community')
            except Exception as e:
                messages.warning(request, 'Update error: {}'.format(e))
        else:
            messages.warning(request, 'You cannot make changes this document you need to be the author')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        form = FeatureCreationForm(instance=feature)
    
    context = {
        'f_form': form,
        'feature': feature
    }
   
    return render(request, 'create_feature.html', context)
    
@login_required
def delete_feature(request, id):
    del_feature = get_object_or_404(Feature, pk=id)
    if request.user == del_feature.author:
        del_feature.delete()
        messages.success(request, 'Feature has been deleted successfully')
        return redirect(reverse('allfeatures'))
    else:
        messages.error(request, 'You are not allowed to delete this Issue')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    