from django.db import models

class PotentialPhotographer(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=128, unique=True)
    lastname = models.CharField(max_length=100)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.email

class PotentialPlanner(models.Model):
    firstname = models.CharField(max_length=100)
    email = models.EmailField(max_length=128, unique=True)
    lastname = models.CharField(max_length=100)
    def __str__(self): # For Python 2, use __unicode__ too
        return self.email
