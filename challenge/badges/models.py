from django.db import models

# Create your models here.
class badges(models.Model):
    picture = models.CharacterField(max_length=200)
    name    = models.CharacterField(max_length=200)


class badgesEarnt(models.Model):
    user    = models.ForeignKey('userprofile.user')
    challenge = models.ForeignKey('challenge.Challenge')
    datetime = models.DateTimeField()
    steps = models.IntegerField(default=0)
