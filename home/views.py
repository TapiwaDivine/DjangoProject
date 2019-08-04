from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

def home(request):
#will render the home page
    return render(request, "index.html")