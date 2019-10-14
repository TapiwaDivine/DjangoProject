from django.shortcuts import render

def get_services_page(request):
    # display services page
    return render(request, "services.html")
