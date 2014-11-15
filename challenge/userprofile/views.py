from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user
from challenge.models import ChallengeParticipation, Challenge

# Create your views here.
def viewProfile(request, user_id):
    u = get_object_or_404(user, pk=user_id)
    context = {'username' : u.name,
               'userage'  : u.age,
               'userlocation' : u.location,
               'usergender'   : u.gender,}
    return render(request, 'userprofile/userprofile.html', context)


def getChallenges(request,user_id):
    c = ChallengeParticipation.objects.filter(user = user_id)
    return HttpResponse(c)
