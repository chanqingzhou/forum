# accounts/urls.py
from django.urls import path
from django.conf.urls import url
from django.contrib.auth.views import (
    login,
    logout,
    password_reset,
    password_reset_done,
    password_reset_confirm
)
from accounts import views as core_views
from . import views
app_name='accounts'

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^timeline/$', views.timeline, name='timeline'),
    url(r'^profile/$', views.view_profile, name='view_profile' ),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^change-password/$', views.change_password, name='change_password'),
    url(r'change-password-invalid/$', views.change_password_invalid, name='change_password_invalid'),
    url(r'^profile/password/$', views.change_password, name='change_password')
    #url(r'^reset-password/$', password_reset, name='reset_password'),
    #url(r'^reset-password/done/$', password_reset_done, name='password_reset_done'),
    #url(r'^reset-password/confirm/$', password_reset_confirm, name='password_reset_confirm')
]