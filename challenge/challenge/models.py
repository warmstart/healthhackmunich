from django.db import models

# Create your models here.

class Challenge(models.Model):
    challenge_name = models.CharField(max_length=200)
    creator = models.CharField(max_length=200)
    stepsgoal = models.IntegerField(default=0)
    deadline = models.DateTimeField()
    
    def __unicode__(self):
        return "{0}".format(self.challenge_name)

#class ChallengeType(models.Model):
    

class ChallengeParticipation(models.Model):
    user = models.ForeignKey('userprofile.user')
    challenge = models.ForeignKey(Challenge)
    steps = models.IntegerField(default=0)
    status = models.CharField(max_length=200)

    def __unicode(self):
        return "{0}".format(self.steps)
