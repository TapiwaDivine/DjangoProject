from django.shortcuts import render
from services.models import Feature

# Create your views here.

def do_search(request):
    feature = Feature.objects.filter(name__icontains=request.GET['q'])
    return render(request, 'display_allfeatures.html', {'features': feature})