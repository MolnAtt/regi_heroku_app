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
    print(request.path)
    print(request.path.split('/'))
    print(utolso_az_urlben)
    szurestipus = utolso_az_urlben if utolso_az_urlben!='valasztas' else ''

    if request.method=="POST":
        poszt = request.POST
        valasztott_foglalkozas = Foglalkozas.objects.get(id=poszt['melyiket'])
        a_felhasznalo = Felhasznalo.objects.get(user=request.user)
        
        if valasztott_foglalkozas.aktletszam() >= valasztott_foglalkozas.letszam:
            alertlista.append("Sajnos ez a foglalkozás közben betelt.")
        else:
            print(request.user)

            try:
                j = Jelentkezes.objects.get(felhasznalo = a_felhasznalo)
                j.foglalkozas = valasztott_foglalkozas
                j.save()
            except Jelentkezes.DoesNotExist:
                Jelentkezes.objects.create(felhasznalo = a_felhasznalo, foglalkozas = valasztott_foglalkozas)
    return render(request, "valasztas.html", {'foglalkozasok': Foglalkozas.lista(szurestipus), 'alertlista': alertlista, 'szurestipus': szurestipus})

