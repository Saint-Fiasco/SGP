__author__ = 'santiago'
from django.conf.urls import patterns, url
from SGPv1 import views
urlpatterns = patterns('',
url(r'^/home', views.home, name='home'),
url(r'^$', views.index, name='index')
)