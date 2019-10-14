from django.conf.urls import url
from .views import logout, login, registration, user_profile

urlpatterns = [
    url('logout', logout, name='logout'),
    url('login', login, name='login'),
    url('signup', registration, name='signup'),
    url('profile', user_profile, name='profile'),
    ]