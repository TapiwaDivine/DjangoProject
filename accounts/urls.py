from django.conf.urls import url
from .views import logout, login, signup

urlpatterns = [
    url(r'^$', logout, name='logout'),
    url(r'^$', login, name='login'),
    url(r'^$', signup, name='signup'),
    ]