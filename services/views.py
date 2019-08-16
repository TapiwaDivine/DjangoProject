from django.shortcuts import render

def get_services(request):
    return render(request, "services.html")
