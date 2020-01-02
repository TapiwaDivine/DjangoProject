from django.conf.urls import url
from .views import checkout

urlpatterns = [
    # url for checkout
    url(r'^$', checkout, name="checkout")
    ]