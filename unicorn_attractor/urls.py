"""unicorn_attractor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import RedirectView
from django.views.static import serve
from .settings import MEDIA_ROOT
from home import urls as urls_home
from services import urls
from accounts import urls as urls_logout
from accounts import urls as urls_login
from accounts import urls as urls_signup
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', RedirectView.as_view(url='home/')),
    url(r'home/', include('home.urls')),
    url(r'^services/', include('services.urls')),
    url(r'^accounts/logout', include('accounts.urls')),
    url(r'^accounts/login', include('accounts.urls')),
    url(r'^accounts/signup', include('accounts.urls')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
]
