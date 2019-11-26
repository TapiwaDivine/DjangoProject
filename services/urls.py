from django.conf.urls import url
from .views import get_services_page, create_feature_page, view_feature_details, render_all_features, edit_feature, delete_feature, like_a_feature_post

urlpatterns = [
    url(r'^$', get_services_page, name='services'),
    url(r'^request_feature/$', create_feature_page, name='request_feature'),
    url(r'^featureview/(?P<id>\d+)/$', view_feature_details, name='featureview'),
    url(r'^like$', like_a_feature_post, name='likes'),
    url(r'^allfeatures/$', render_all_features, name='allfeatures'),
    url(r'^edit_feature/(?P<id>\d+)/$', edit_feature, name='edit_feature'),
    url(r'^delete_feature/(?P<id>\d+)/$', delete_feature, name='delete_feature'),
    ]