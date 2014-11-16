from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user
from challenge.models import ChallengeParticipation, Challenge

from userprofile.views import viewProfile

# Create your views here.
def listChallenges(request):
    c = Challenge.objects.all()
    context = {'challenges' : c,
               'user_id' : "1"}
    return render(request, 'challenge/challenge-list.html', context)


def joinChallenge(request, user_id, chall_id):
    c = Challenge.objects.get(id=chall_id)
    u = user.objects.get(id=user_id)
    cp = ChallengeParticipation(user=u, challenge=c, status='active');
    cp.save()
   
    return viewProfile(request, user_id)
