from django.shortcuts import render
from django.template import Context, Template
from .models import *

########################## SEGÉDFÜGGVÉNYEK ##############################

def orarend_kontextus(html, cssek, **kwargs):
    kontextus = {        
        'napok': Nap.objects.all(),
        'hanyadikok': range(0,10),
        'a_html': html,
        'cssek': cssek,
    }
    kontextus.update(kwargs)
    return kontextus

def beolvas(honnan) -> str:
    with open(f'APP/templates/{honnan}', mode='r', encoding='utf-8') as templatehtml:
        return templatehtml.read()

def kiir(hova, mit) -> None:
    with open(f'APP/templates/{hova}', mode='w', encoding='utf-8') as preparedhtml:
        preparedhtml.write(mit)

def prepare_or_serve(request, rendernow, template, prepared, context):
    if rendernow=='rendernow':
        kiir(prepared, str(Template(beolvas(template)).render(Context(context))))        
    return render(request, prepared,{})

##################################################################################

def nagy_dor(request, rendernow):
    return prepare_or_serve(request, rendernow, 'orarend/base.html', 'orarend/prepared/nagy_dor.html', 
        orarend_kontextus('orarend/nagy_dor.html',['orarend/css/nagy.css', 'orarend/css/nagy_dor.css'], 
            osztalyok=sorted(filter(lambda onev: onev.kreta!= '-', Osztaly.objects.all()), key=lambda x:x.sorszam)))

def nagy_teor(request, rendernow):
    return prepare_or_serve(request, rendernow, 'orarend/base.html', 'orarend/prepared/nagy_teor.html', 
        orarend_kontextus('orarend/nagy_teor.html',['orarend/css/nagy.css', 'orarend/css/nagy_teor.css'], 
            termek=sorted(Terem.objects.all(), key=lambda x:x.sorszam)))

def nagy_tor(request, rendernow):
    return prepare_or_serve(request, rendernow, 'orarend/base.html', 'orarend/prepared/nagy_tor.html', 
        orarend_kontextus('orarend/nagy_tor.html',['orarend/css/nagy.css', 'orarend/css/nagy_tor.css'], 
            tanarok=sorted(Tanar.objects.all(), key=lambda x:x.sorszam)))

