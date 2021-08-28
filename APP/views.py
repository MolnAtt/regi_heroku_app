from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Foglalkozas, Jelentkezes, Felhasznalo

def index(request):
    return render(request, "index.html", {})

def urlap(request):
    return redirect('https://forms.gle/m83fFTCivQLD4KZR6')

@login_required
def valasztas(request):
    alertlista = []
    utolso_az_urlben = request.path.split('/')[-2]
    szurestipus = utolso_az_urlben if utolso_az_urlben!='valasztas' else ''

    a_felhasznalo = Felhasznalo.getuser(request)

    if request.method=="POST":

        poszt = request.POST
        print(poszt)
        valasztott_foglalkozas = Foglalkozas.objects.get(id=poszt['melyiket'])
        
        if poszt['mitcsinal']=='lejelentkezes':
            a_felhasznalo.jelentkezese().delete()
            korabban_valasztott_foglalkozas_id = "nincs"
        elif poszt['mitcsinal'] in ['jelentkezes', 'atjelentkezes']:
            if valasztott_foglalkozas.aktletszam() >= valasztott_foglalkozas.letszam:
                alertlista.append("Sajnos ez a foglalkozás közben betelt. (Valaki(k) már rákattintott(ak) erre azóta, hogy betöltötted az oldalt.)")
            else:
                try:
                    j = a_felhasznalo.jelentkezese()
                    j.foglalkozas = valasztott_foglalkozas
                    j.save()
                except Jelentkezes.DoesNotExist:
                    Jelentkezes.objects.create(felhasznalo = a_felhasznalo, foglalkozas = valasztott_foglalkozas)

                korabban_valasztott_foglalkozas_id = valasztott_foglalkozas.id
    else: # request.method=="GET":
        try:
            korabban_valasztott_foglalkozas_id = a_felhasznalo.foglalkozasa().id
        except Jelentkezes.DoesNotExist:
            korabban_valasztott_foglalkozas_id = "nincs"
    return render(request, "valasztas.html", {
        'foglalkozasok': Foglalkozas.lista(szurestipus, request), 
        'alertlista': alertlista, 
        'szurestipus': szurestipus, 
        'korabban_valasztott_foglalkozas_id':korabban_valasztott_foglalkozas_id
        })

@login_required
def nevsor(request):
    utolso_az_urlben = request.path.split('/')[-2]
    a_foglalkozas = Foglalkozas.objects.get(kod = utolso_az_urlben)
    return render(request, "nevsor.html", {'nevsor': a_foglalkozas.nevsora(), 'a_foglalkozas': a_foglalkozas})
