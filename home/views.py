from django.shortcuts import render

def index(request):
#will render the home page
    return render(request, "index.html")
    