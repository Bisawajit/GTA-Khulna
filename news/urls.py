from django.conf.urls import patterns, include, url
from news.views import *

urlpatterns = patterns('',
    url(r'^$', ListNews.as_view(), name='newslist'),
    url(r'^page(\d+)$', ListNews.as_view(), name='newslist'),
    url(r'^create$', CreateNews.as_view(), name='newsform'),
)
