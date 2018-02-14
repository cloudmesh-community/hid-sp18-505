""" SRER app urls.
"""
from django.conf.urls import url, include
from .views import IndexView

app_name='home'
urlpatterns = [
    url(r'^\Z', IndexView.as_view(), name='index'),
]