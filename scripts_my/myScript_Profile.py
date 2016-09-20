# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', '..\Raduga02.settings')


import django
django.setup()

from app.models import CommonModel, Member, Place_departure_choices, Residing, Participation , Director, News
from app.forms import UserRegistrationForm, MemberForm , ParticipationForm,ResidingForm, TransferForm, ExcursionForm
from django.contrib.auth.models import User

from django import forms
import simplejson
from django.core import serializers

from django.core.mail import send_mail
from django.template.loader import render_to_string

from os import path
PROJECT_ROOT = path.dirname(path.abspath(path.dirname(__file__)))
print PROJECT_ROOT
print path.join(PROJECT_ROOT, 'Raduga02', 'app','templates')
#print STATIC_ROOT



print "###############################################################################################"

ps1 = Participation.objects.filter(age_group='0-7')

Profile_data = {
    'country' : 'россия',
    'region': 'Чувашская Республика',
    'city': 'Чебоксары',
    'street':  'Молодежная',
    'homeNumber': '24' 
}

dir2 = Director.objects.create(Profile_data)

print dir2 

# Member.objects.create(user_id = 2, age_group='0-7', first_name='fname1',last_name='lname1', age=4,gender='male',scan_passport='ваваfgfg.jpg')

# mems =  Member.objects.filter(user_id = 2)
# for mem in mems:
    # print u'{0}'.format(mem.scan_passport)

# data = {
            # #'tour_form' : 'EveningCheb',
            # 'date_departure':   '2015-10-27', 
            # 'time_departure':   '02:10:00',
            # 'place_departure':  -1,
            # 'place_arrival':    -2,
            # 'quantity_total':   '34',
            # 'quantity_adult':   '4',
            # 'quantity_member':  '30'
          # }
# f = MemberForm(MemberData)
# res = f.save(commit=False)
# res.user_id = 2
# f.is_valid()
# print f.is_valid()
# # # all = f.cleaned_data['quantity_total']
# f.save()
# dir = Director.objects.get(user_id = 3)
# print dir.email
# if Director.objects.get(user_id = 3).email in ['', None]:
    # print 'email is empty'

#print Director.objects.filter(is_superuser = 1)  #filter()
#Member.objects.filter(participation__id = app.id)






                
