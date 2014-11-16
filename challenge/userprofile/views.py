from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user
from challenge.models import ChallengeParticipation
from badges.models import badges, badgesEarnt

import logging
import datetime


logger = logging.getLogger(__name__)

# Create your views here.
def viewProfile(request, user_id):
    u = get_object_or_404(user, pk=user_id)
    c = ChallengeParticipation.objects.filter(user=user_id)
    cforrender = []
    fcforrender = []
    for challenge in c:
        onechall = {}
        thischall = challenge.challenge
        
        onechall['name'] = thischall.challenge_name
        onechall['progress'] = min(100 * (challenge.steps / float(thischall.stepsgoal) ),100)
        onechall['description'] = thischall.description 
        
        if challenge.status != "finished":
            cforrender.append(onechall)
        elif challenge.status == "finished":
            fcforrender.append(onechall)

    b = badgesEarnt.objects.filter(user=user_id)
    bforrender = []
    for badge in b:
        onebadge = {}
        thisbadge = badge.badge

        onebadge['picture'] = thisbadge.picture
        onebadge['name']    = thisbadge.name
        onebadge['date']    = badge.datetime
        bforrender.append(onebadge)

    context = {'username': u.name,
               'userage': u.age,
               'userlocation': u.location,
               'usergender': u.gender,
               'challenges': cforrender, 
               'fchallenges': fcforrender, 
               'badges'     : bforrender,}
    return render(request, 'userprofile/userprofile.html', context)


def getChallenges(request, user_id):
    c = ChallengeParticipation.objects.filter(user=user_id)
    return HttpResponse(c)


def landing(request):
    return render(request, 'challenge/landing.html', [])


def addSteps(request, user_id, steps):
    participations = ChallengeParticipation.objects.filter(user=user_id)
    logger.debug(participations)
    for c in participations:
        c.steps += int(steps)
        if ((c.challenge.stepsgoal <= c.steps) and (c.status != "finished")):
            c.status = "finished"
            b = badgesEarnt(user=user.objects.get(id=user_id), challenge=c.challenge, datetime=datetime.datetime.now(), steps=c.steps, badge=badges.objects.get(id=1))
            b.save()
        c.save()
    return viewProfile(request, user_id)

