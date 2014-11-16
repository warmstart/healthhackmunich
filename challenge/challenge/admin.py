from django.contrib import admin
from challenge.models import Challenge, ChallengeParticipation
from userprofile.models import user
from badges.models import badges, badgesEarnt


# Register your models here.
admin.site.register(Challenge)
admin.site.register(ChallengeParticipation)
admin.site.register(user)
admin.site.register(badges)
admin.site.register(badgesEarnt)
