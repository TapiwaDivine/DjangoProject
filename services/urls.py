from django.conf.urls import url
from .views import get_services

urlpatterns = [
    url(r'^$', get_services, name='services'),
    ]