# -*- coding: utf-8 -*-

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Raduga02.settings')


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
CASE_SQL = '(case when form_of_execution="solo" then 1 \
                    when form_of_execution="duet" then 2 \
                    when form_of_execution="ensamble" then 3 end)'   # для сортировки по форме исполнения в нативном скл 

def template_args_child( _age_prefix , _prefix_t , rnd_flag = False):  # в шаблоне нельзя использовать знак "-" поэтмо казываю сам префикс
    _nom_list = ['estrada', 'narod+_narod_style', 'suget_igrovoi', 'spec']
    _f_ex = ['solo', 'duet', 'ensamble'] 
    
    _args = {}        # хранение переменных для шаблона
    
    CASE_SQL = '(case when form_of_execution="solo" then 1 \
                    when form_of_execution="duet" then 2 \
                    when form_of_execution="ensamble" then 3 end)'   # для сортировки по форме исполнения в нативном скл 
    
    _p = Participation.objects.filter(age_group=_age_prefix) #.\
        #extra(select={'f_execution': CASE_SQL}, order_by=['f_execution'])
    for nom in _nom_list:
        _q = _p.filter(nomination = nom)
        _list_parton = []
        _args['age_' + _prefix_t +'_' + nom] = _list_parton
        
        for fex in _f_ex:        
            _list_parton.append(_q.filter(form_of_execution=fex) )         
    print _args
    print "=afterg=="
    return _args    
    
ps1 = Participation.objects.filter(age_group='0-7')

my_sets = template_args_child('0-7', '0_7' , False)
for k,v in my_sets.iteritems():
    print k
    print v
    print "----"
print "-----middle----------"

    

estrada1 = ps1.filter(nomination = 'estrada').extra(select={'f_execution': CASE_SQL}, order_by=['f_execution'])    
# print ps1
# for i in estrada1:
    # print u'{0} , {1} , {2}'.format(i, i.form_of_execution, i.nomination)
# print "----------"
# print "======"
es_res = []
estrada2 = ps1.filter(nomination = 'estrada') #.extra(select={'f_execution': CASE_SQL}, order_by=['f_execution'])
# es2solo = estrada2.filter(form_of_execution='solo').order_by('?')
# es2duet = estrada2.filter(form_of_execution='duet').order_by('?')
# es2ensamble = estrada2.filter(form_of_execution='ensamble').order_by('?')
# for i in es2solo:
    # es_res.append(i)
# for i in es2duet:
    # es_res.append(i)
# for i in es2ensamble:
    # es_res.append(i)

def filter_by_form(_qset):
    _res = []
    _res_solo = _qset.filter(form_of_execution='solo').order_by('?')
    _res_duet = _qset.filter(form_of_execution='duet').order_by('?')
    _res_ensamble = _qset.filter(form_of_execution='ensamble').order_by('?')
    for i in _res_solo:
        _res.append(i)
    for i in _res_duet:
        _res.append(i)
    for i in _res_ensamble:
        _res.append(i)
    return _res


    
# for i in filter_by_form(estrada2):
    # print u'{0} , {1} , {2}'.format(i, i.form_of_execution, i.nomination)
# print "----------"

# ps2 = ps1.order_by('?')
# for i in ps2:
    # print u'{0} , {1}'.format(i, i.form_of_execution)
# print
# CASE_SQL = '(case when form_of_execution="solo" then 1 \
                        # when form_of_execution="duet" then 2 \
                        # when form_of_execution="ensamble" then 3 end)' 
# ps = Participation.objects.extra(select={'f_execution': CASE_SQL}, order_by=['f_execution'])
#filter(nomination = 'estrada')
# print ps
# for i in ps:
    # print u'{0} , {1}'.format(i, i.form_of_execution)
# fr = forms.ModelForm()
# print ModelForm
# _news = News.objects.all().order_by('-date_creation')[:5]
# print _news

#print Member.objects.get(id=1).scan_passport

# print Participation.objects.filter(user_id = 71)
# for parton in Participation.objects.filter(user_id = 71):
    # print parton
#dir.email = 
#news = News.objects.filter(id="17")
#news.news_title = "new_title_4"
#news.save()
# print news.foto
# print news.foto.url
# print news.foto.path



# MemberData = {
    # 'age_group': '0-7',
    # 'first_name': 'fname1',
    # 'last_name': 'lname1',
    # 'age': '4',
    # 'gender': 'male',
    # 'scan_passport': 'fgfg'
        
# }
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

# новости - рассылка
# context = {'news' : news }           #'news_title': news.news_title, 'news.foto.url', 'message': message}
# html = render_to_string('app/news_for_mail.html', context)
# mails =  User.objects.filter(is_superuser = 1).values_list('email', flat=True)
# for mail in mails:
    # try:
        # if mail not in ['', None]:
            # print mail
            # send_mail('Новости. "Радуга-танца" г.Чебоксары' , u'Коллектив {0}'.format('del2'),
                      # 'dance@radugafest.com', [mail], fail_silently=False,
                      # html_message=html)
    # except Exception as ex:
        # print ex.message

#print Director.objects.all().values_list('email', flat=True)

#print Director.objects.filter(user__email = 'romantix74@list.ru')





                
