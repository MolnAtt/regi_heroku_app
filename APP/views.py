from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Foglalkozas, Jelentkezes, Felhasznalo, Vezerlo, Osztaly


def index(request):
    alertlista = [] 
    karbantartas_ideje = Vezerlo.objects.get(kod='karbantartasjelzes').nev
    if karbantartas_ideje != '0':
        alertlista.append(f"Az oldalon jelenleg karbantartás zajlik, így átmenetileg nem lehet bejelentkezni. Nézz vissza {karbantartas_ideje} perc múlva.")
    return render(request, "index.html", {
        'backend_uzenetek': alertlista, 
        })

def urlap(request, melyik):
    return redirect('https://forms.gle/m83fFTCivQLD4KZR6')

def foindex(request):
    return redirect(f'http://{request.get_host()}/tesi/')

@login_required
def valasztas(request, szurestipus=""):
    alertlista = []
    # utolso_az_urlben = request.path.split('/')[-2]
    # szurestipus = utolso_az_urlben if utolso_az_urlben!='valasztas' else ''

    a_felhasznalo = Felhasznalo.getuser(request)

    
    uzemmod = {
        'fel': a_felhasznalo.feljelentkezhet, 
        'le':  a_felhasznalo.lejelentkezhet, 
        'at':  a_felhasznalo.atjelentkezhet,
        }
    
    # üzemmód: 000-111, a három opció: fel-, le-, átjelentkezés
    if request.method=="POST" and (uzemmod['fel'] or uzemmod['le'] or uzemmod['at']):

        poszt = request.POST
        valasztott_foglalkozas = Foglalkozas.objects.get(id=poszt['melyiket'])
        
        if poszt['mitcsinal']=='lejelentkezes':
            if uzemmod['le']:
                a_felhasznalo.jelentkezese().delete()
                alertlista.append("A foglalkozásról sikeresen lejelentkeztél.")
                korabban_valasztott_foglalkozas_id = "nincs"
            else: 
                alertlista.append("Jelenleg nem tudsz lejelentkezni.")
                korabban_valasztott_foglalkozas_id = valasztott_foglalkozas

        elif poszt['mitcsinal'] in ['jelentkezes', 'atjelentkezes']:
            if valasztott_foglalkozas.aktletszam() >= valasztott_foglalkozas.letszam:
                korabban_valasztott_foglalkozas_id = "mindegysajnos"
                alertlista.append("Sajnos ez a foglalkozás közben betelt. Valaki(k) már rákattintott(ak) erre azóta, hogy betöltötted az oldalt.")
            else:
                try:
                    if uzemmod['at'] or uzemmod['fel']:
                        j = a_felhasznalo.jelentkezese()
                        if uzemmod['at']:
                            j.foglalkozas = valasztott_foglalkozas
                            j.save()
                            alertlista.append("A foglalkozásra való átjelentkezés sikeres volt.")
                        else:
                            alertlista.append("Jelenleg nem tudsz átjelentkezni.")
                except Jelentkezes.DoesNotExist:
                    if uzemmod['fel']:
                        Jelentkezes.objects.create(felhasznalo = a_felhasznalo, foglalkozas = valasztott_foglalkozas)
                        alertlista.append("A foglalkozásra való jelentkezés sikeres volt.")
                    else:
                        alertlista.append("Jelenleg nem tudsz jelentkezni.")

                korabban_valasztott_foglalkozas_id = valasztott_foglalkozas.id
    else: # request.method=="GET":
        try:
            korabban_valasztott_foglalkozas_id = a_felhasznalo.foglalkozasa().id
        except Jelentkezes.DoesNotExist:
            korabban_valasztott_foglalkozas_id = "nincs"
    return render(request, "valasztas.html", {
        'foglalkozasok': Foglalkozas.lista(szurestipus, request), 
        'backend_uzenetek': alertlista, 
        'szurestipus': szurestipus, 
        'korabban_valasztott_foglalkozas_id':korabban_valasztott_foglalkozas_id,
        'uzemmod': uzemmod,
        'megtelt_e': uzemmod,
        })

@login_required
def nevsor(request, a_kod):
    a_foglalkozas = Foglalkozas.objects.get(kod = a_kod)
    return render(request, "nevsor.html", {'felhasznalok': a_foglalkozas.felhasznaloi(), 'cim': a_foglalkozas.nev})

@login_required
def nemjelentkeztek(request):
    return render(request, "nevsor.html", {'felhasznalok': Felhasznalo.akik_nem_jelentkeztek(), 'cim': 'nem jelentkeztek'})

@login_required
def attekintes(request:HttpRequest, template, rendezes="nev") -> HttpResponse:
    return render(request, f"attekintes_{template}.html", {
        'jelentkezesek': Jelentkezes.ek_attekintese(rendezes.split('_')), 
        })
