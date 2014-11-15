from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse


# Create your views here.
def viewProfile(request, user_id):
    u = get_object_or_404(pk=user_id)
    return render(request, 'userprofile/layout.html', u)
