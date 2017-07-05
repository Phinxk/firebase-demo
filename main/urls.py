"""Contain url patterns for main app."""

from django.conf import settings
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^register-device/$', views.register_device, name='register_device'),
    url(r'^delete-device/$', views.delete_device, name='delete_device'),
]
