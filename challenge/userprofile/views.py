from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user
from challenge.models import ChallengeParticipation
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def viewProfile(request, user_id):
    u = get_object_or_404(user, pk=user_id)
    c = ChallengeParticipation.objects.filter(user=user_id)
    cforrender = []
    for challenge in c:
        onechall = {}
        thischall = challenge.challenge

        onechall['name'] = thischall.challenge_name
        onechall['progress'] = min(100 * (challenge.steps / float(thischall.stepsgoal) ),100)
        onechall['description'] = "blablabla"
        cforrender.append(onechall)

    context = {'username': u.name,
               'userage': u.age,
               'userlocation': u.location,
               'usergender': u.gender,
               'challenges': cforrender, }
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
        c.save()
    return viewProfile(request, user_id)

