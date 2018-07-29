# accounts/urls.py
from django.urls import path
from django.conf.urls import url
from accounts import views as core_views
from . import views
app_name='accounts'

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^profile/$', views.view_profile, name='view_profile' ),
    url(r'profile/edit/$', views.edit_profile, name='edit_profile'),
]