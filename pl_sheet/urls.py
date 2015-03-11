from django.conf.urls import patterns, include, url
from players.views import *
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin', include(admin.site.urls)),
    url(r'^championship/$', ChampionshipView.as_view(), name='frontend_championship'),
    url(r'^', HomeView.as_view(), name='frontend_home'),



)
