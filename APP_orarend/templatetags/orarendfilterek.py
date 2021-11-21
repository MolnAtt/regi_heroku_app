from django import template
# from datetime import datetime
from babel.dates import format_date, format_datetime, format_time
from APP_orarend.models import *

register = template.Library()

@register.filter(name='szep_szazalek')
def szep_szazalek(szam):
    if (szam.is_integer()):
        return f'{int(szam)}%'
    return f'{szam}%'

@register.filter(name='bol')
def bol(mibol, mit):
    return mibol - mit

@register.filter(name='ehn')
def ehn(datum):
    return format_datetime(datum, "yyyy.MM.dd (EEEE)", locale='hu_HU')
    # return datum.strftime('%Y.%m.%d (%a)')

@register.simple_tag
def orak(**kwargs):
    return Ora.objects.filter(**kwargs)

@register.simple_tag
def orak_dor(**kwargs):
    # if kwargs['osztaly'].sorszam!=3:
    #     return []
    return kwargs['osztaly'].orai_ilyenkor(kwargs['nap'], kwargs['ora'])

@register.filter(name='pont_melle_szokoz')
def pont_melle_szokoz(szoveg):
    return szoveg.replace(".", ". ")

@register.filter(name='hagyomanyos')
def hagyomanyos(s):
    return s if s!="nya" else "kny"
