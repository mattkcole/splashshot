import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
        'picsite.settings')

import django
django.setup()

from splash.models import PotentialPhotographers

#def populate():
#    emails = []
