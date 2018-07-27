# accounts/urls.py
from django.urls import path
from django.conf.urls import url
from accounts import views as core_views
from . import views
app_name='accounts'

urlpatterns = [
    url(r'^signup/$', core_views.signup, name='signup'),
    path('profile/', views.profile, name='profile' ),
    url(r'^timeline/$', views.timeline, name='timeline'),
]