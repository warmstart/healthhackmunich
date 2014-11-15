from django.db import models

# Create your models here.
class user(models.Model):
    name = models.CharField(max_length=50)
    picture = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=1)

    def __unicode__( self ):
        return "{0}".format(self.name)
