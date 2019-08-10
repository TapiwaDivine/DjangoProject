from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.utils import timezone

def home(request):
#will render the home page
    return render(request, "index.html")
    
def services(request):
#will render the home page
    return HttpResponse("<h1>Hello World</h1>")