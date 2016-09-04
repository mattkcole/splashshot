from django.forms import ModelForm
from django import forms
from django.db import models
from splash.models import PotentialPhotographers


class PhotographerForm(forms.ModelForm):
    email = forms.EmailField(max_length=128,
    help_text="Please enter your email.")
    firstname = forms.CharField(max_length=128)
    lastname = forms.CharField(max_length=128)
    prob = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        # Provide an association between the ModelForm and a model
        model = PotentialPhotographers
        fields = ('email',)
