from django.db import models

class PotentialPhotographers(models.Model):
    email = models.EmailField(max_length=128, unique=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    prob = models.IntegerField()
    def __str__(self): # For Python 2, use __unicode__ too
        return self.email
