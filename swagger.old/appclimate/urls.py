from django.conf.urls import url, include
from django.urls import path
from .views import IndexView, RaingageApiView, PrecipEventApiView


app_name='home'
urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'api/v1.0/raingages/', RaingageApiView.as_view(), name='api_raingages'),
    path(r'api/v1.0/precipevents/', PrecipEventApiView.as_view(), name='precipevents'),
]