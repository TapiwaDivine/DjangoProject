from django.conf.urls import url
from .views import logout, login, signup

urlpatterns = [
    url(r'^logout$', logout, name='logout'),
    url(r'login^$', login, name='login'),
    url(r'signup^$', signup, name='signup'),
    ]