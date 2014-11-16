from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user
from challenge.models import ChallengeParticipation, Challenge

# Create your views here.
def listChallenges(request):
    c = Challenge.objects.all()
    context = {'challenges' : c}
    return render(request, 'challenge/challenge-list.html', context)
