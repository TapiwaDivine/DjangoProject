from django.conf.urls import url
from .views import get_services_page, create_feature_page, view_feature_details, render_all_features

urlpatterns = [
    url(r'^$', get_services_page, name='services'),
    url(r'^request_feature/$', create_feature_page, name='request_feature'),
    url(r'^featureview/(?P<id>\d+)/$', view_feature_details, name='featureview'),
    url(r'^allfeatures/$', render_all_features, name='allfeatures'),
    ]