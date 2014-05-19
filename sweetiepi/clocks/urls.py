from __future__ import absolute_import

from django.conf.urls import patterns, url

from clocks import views

urlpatterns = patterns('',
    # ex: /clocks/
    url(r'^$', views.index, name='index'),
    # ex: /clocks/5/
    url(r'^(?P<clock_id>\d+)/$', views.detail, name='detail'),
)