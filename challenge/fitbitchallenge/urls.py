from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import userprofile.views
import challenge.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fitbitchallenge.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<user_id>\d+)/$', userprofile.views.viewProfile, name='viewProfile'),
    url(r'^getChallenges/(?P<user_id>\d+)$', userprofile.views.getChallenges, name='getChallenges'),
    url(r'^listChallenges/', challenge.views.listChallenges, name='listChallenges'),
    url(r'^joinChallenge/(?P<user_id>\d+)/(?P<chall_id>\d+)/$', challenge.views.joinChallenge, name='joinChallenge'),
    url(r'^addSteps/(?P<user_id>\d+)/(?P<steps>\d+)/$', userprofile.views.addSteps, name='addSteps'),
    url(r'^', userprofile.views.landing, name='landing'),
)
