from django.contrib import admin
from challenge.models import Challenge, ChallengeParticipation
from userprofile.models import user

# Register your models here.
admin.site.register(Challenge)
admin.site.register(ChallengeParticipation)
admin.site.register(user)
