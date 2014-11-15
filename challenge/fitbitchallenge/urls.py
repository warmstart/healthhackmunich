from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import userprofile.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fitbitchallenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user_id>\d+)/$', userprofile.views.viewProfile, name='viewProfile'),
)
