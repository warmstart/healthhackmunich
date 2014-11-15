from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from userprofile.models import user

# Create your views here.
def viewProfile(request, user_id):
    u = get_object_or_404(user, pk=user_id)
    return render(request, 'userprofile/userprofile.html', u)
