from django.shortcuts import render

def get_services(request):
    # display services page
    return render(request, "services.html")
