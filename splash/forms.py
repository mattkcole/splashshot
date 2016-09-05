from django.forms import ModelForm
from django import forms
from django.db import models
from splash.models import PotentialPhotographers


class PhotographerForm(forms.ModelForm):
    firstname = forms.CharField(max_length=128,
    help_text="What's your first name?")
    email = forms.EmailField(max_length=128,
    help_text="Please enter your email.")

    lastname = forms.CharField(widget=forms.HiddenInput(), max_length=128, initial="uk")
    class Meta:
        # Provide an association between the ModelForm and a model
        model = PotentialPhotographers
        fields = ('email',)
