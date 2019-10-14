from django.conf.urls import url
from .views import get_services_page

urlpatterns = [
    url(r'^$', get_services_page, name='services'),
    ]