"""
URL patterns / routes

"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

import duplicateimagecheckapp.receivers

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)
