# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Raduga02.settings')


import django
django.setup()

from app.models import Director, Member, Place_departure_choices, Residing, Participation , \
                    News, Place_residing_choices, Food, Transfer, Excursion
from app.forms import UserRegistrationForm, MemberForm , ParticipationForm,ResidingForm, TransferForm, ExcursionForm, \
                        DirectorEditForm
from django.contrib.auth.models import User

from django import forms
import simplejson
from django.core import serializers

from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import render

from os import path
PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))

print PROJECT_ROOT
print path.join(PROJECT_ROOT, 'Raduga02', 'app','templates', 'tables', 'Profile.html')

print 'tables\Profile.html'

print "###############################################################################################"

args = {}
args['formEditDir'] = DirectorEditForm()
f = DirectorEditForm()

#print render(None, 'tables\Profile.html', args)
print  str(f.helper.label_class)

for i in f.helper.layout:
    print str(i)