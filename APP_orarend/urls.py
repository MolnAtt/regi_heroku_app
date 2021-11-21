from django.contrib import admin
from django.urls import path
from django.shortcuts import render, redirect
from .views import *


urlpatterns = [
    path('', lambda x: render(x, "orarend/linkek.html", {'linkek': [
            {'urlkod': 'nagy', 'nev':'Nagy órarendek'},
            # {'urlkod': 'csoportos', 'nev': 'Csoportosított órarendek'},
            {'urlkod': 'kis', 'nev': 'Kis órarendek'},
        ]})),
    path('<str:meret>/', lambda x,meret: render(x, "orarend/linkek.html", {'linkek': [
            {'urlkod': 'tanar', 'nev': 'Tanárok órarendjei'},
            {'urlkod': 'terem', 'nev': 'Termek órarendjei'},
            {'urlkod': 'diak' , 'nev': 'Osztályok órarendjei'},
        ]})),
    # NAGY ÓRARENDEK (statikus kiszolgálás)
    path('nagy/tanar/', lambda request: redirect('statikus/')), 
    path('nagy/terem/', lambda request: redirect('statikus/')), 
    path('nagy/diak/', lambda request: redirect('statikus/')), 
    # NAGY ÓRARENDEK (helyben renderelés lehetőségével)
    path('nagy/terem/<str:rendernow>/', nagy_teor),
    path('nagy/tanar/<str:rendernow>/', nagy_tor),
    path('nagy/diak/<str:rendernow>/', nagy_dor),
    # KIS ÓRARENDEK dispatcherei
    path('kis/tanar/', lambda request: render(request, "orarend/linkek.html", {
        'linkek': list(map(lambda tanar: {
            'urlkod':tanar.urlkod, 
            'nev':tanar.kreta
            }, sorted(Tanar.objects.all(), key=lambda t: t.kreta)))
        })),
    path('kis/terem/', lambda request: render(request, "orarend/linkek.html", {
        'linkek': list(map(lambda terem: {
            'urlkod':terem.urlkod, 
            'nev':terem.kreta,
            'classname': f'emelet_{terem.emelet}',
            }, Terem.objects.all())),
        'extracssek': ['orarend/css/kis_teor_dispatcher.css']
        })),
    path('kis/diak/', lambda request: render(request, "orarend/linkek.html", {
        'linkek': list(map(lambda osztaly: {
            'urlkod': osztaly.urlkod, 
            'nev': osztaly.kreta,
            'classname': 'o'+osztaly.urlkod,
            }, filter(lambda onev: onev.kreta!= '-', Osztaly.objects.all()))),
        'extracssek': ['orarend/css/kis_dor_dispatcher.css']
        })),
    # KIS ÓRARENDEK maguk
    path('kis/tanar/<str:tanar_urlkod>/', lambda request, tanar_urlkod: render(request, "orarend/base.html", 
        orarend_kontextus('orarend/kis_tor.html', ['orarend/css/kis_tor.css'], a_tanar=list(filter(lambda tanar: tanar.urlkod == tanar_urlkod , Tanar.objects.all()))[0]))),
    path('kis/terem/<str:terem_urlkod>/', lambda request, terem_urlkod: render(request, "orarend/base.html", 
        orarend_kontextus('orarend/kis_teor.html', ['orarend/css/kis_teor.css'], a_terem=list(filter(lambda terem: terem.urlkod == terem_urlkod , Terem.objects.all()))[0]))),
    path('kis/diak/<str:osztaly_urlkod>/', lambda request, osztaly_urlkod: render(request, "orarend/base.html", 
        orarend_kontextus('orarend/kis_dor.html', ['orarend/css/kis_dor.css'], az_osztaly=list(filter(lambda osztaly: osztaly.urlkod == osztaly_urlkod , Osztaly.objects.all()))[0]))),
]