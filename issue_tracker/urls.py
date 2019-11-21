from django.conf.urls import url
from .views import render_contact_us_page, display_community_page, bug_form_page, view_bug_details, render_all_bugs, edit_issue, delete_issue, BugLikeToggle

urlpatterns = [
    url(r'^contact_us$', render_contact_us_page, name='contact_us'),
    url(r'^community$', display_community_page, name='community'),
    url(r'^bugform/$', bug_form_page, name='bugform'),
    url(r'^viewissue/(?P<id>\d+)/$', view_bug_details, name='viewissue'),
    url(r'^viewissue/(?P<id>\d+)/like/$', BugLikeToggle.as_view(), name="like"),
    url(r'^allissues/$', render_all_bugs, name='allissues'),
    url(r'^edit_issue/(?P<id>\d+)/$', edit_issue, name='edit_issue'),
    url(r'^delete_issue/(?P<id>\d+)/$', delete_issue, name='delete_issue')
    
    ]