from django.conf.urls import url, include
from .views import hello, resttest
urlpatterns = [
    url(r'^hello/$', hello),
    url(r'^resttest/$', resttest)
]