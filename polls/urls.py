"""
    Url configuration file for polls app
    Link Django views to urls within app
"""

from django.conf.urls import url
from . import views

# Disable pylint warning for variables treated as constants
# pylint: disable=C0103

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
