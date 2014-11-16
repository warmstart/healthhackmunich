from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user
from challenge.models import ChallengeParticipation, Challenge

# Create your views here.
def viewProfile(request, user_id):
    u = get_object_or_404(user, pk=user_id)
    c = ChallengeParticipation.objects.filter(user=user_id)
    cforrender = []
    for challenge in c:
        onechall = {}
        thischall = challenge.challenge

        onechall['name'] = thischall.challenge_name
        onechall['progress'] = 100 * (challenge.steps / float(thischall.stepsgoal) )
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
    return viewProfile(request, user_id)

