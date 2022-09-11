from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Jelentkezes, Felhasznalo, Osztaly, Foglalkozas, Vezerlo
from datetime import datetime, timedelta
from django.contrib.auth.hashers import make_password
from levelkuldes import levelkuldes_dir
from django.template import Context, Template
from re import sub


admin.site.register(Jelentkezes)
admin.site.register(Foglalkozas)
admin.site.register(Osztaly)

# a trükkös admin-funkciókról, függvényekről az szlgbp_ma_heroku gitrepoban vannak jó példák.


# metódusok, amelyekre szükség van: 
# - Felhasználók beolvasása

### Beépített user-modellre épített két-modelles userszerkezet feltöltése és csoporthozzárendelése ###
def userek_beolvasasa(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        fajlnev = f"txt/userek/{vezerlo.kod}_userinput.csv" # a [...]_userinput.csv feltétlen tartalmazza az (ékezetmentes stb.?) mezőneveket!
        with open(fajlnev, 'r', encoding="utf-8") as f:
            mezonevek = f.readline().strip().split(';')
            for sor in f:
                sorszotar = dict(zip(mezonevek, sor.strip().split(';')))

                az_osztaly = Osztaly.objects.get_or_create(kod=sorszotar['osztalykod'], nev=sorszotar['osztalynev'])[0]
                
                try:
                    a_user = User.objects.get(username=sorszotar['email'])
                except User.DoesNotExist:
                    a_user = User.objects.create_user(username=sorszotar['email'], email=sorszotar['email'], password=sorszotar['password'], is_active=False)

                Felhasznalo.objects.get_or_create(nev=sorszotar['nev'], user=a_user, osztaly=az_osztaly)[0]

                for a_csoport in map(lambda csoportnev: Group.objects.get_or_create(name=csoportnev)[0], sorszotar['groups'].split(',')):
                    a_user.groups.add(a_csoport)
                
        print(f'{vezerlo.nev} vezérlő usereinek a beolvasása sikeres')
userek_beolvasasa.short_description = "USEREK feltöltése [vezerlo.kod]_userinput.csv-ből"



def foglalkozasok_beolvasasa(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        #try:
        fajlnev = f"txt/foglalkozasok/{vezerlo.kod}_foglalkozasinput.csv"

        with open(fajlnev, 'r', encoding="utf-8") as f:
            #i=0
            for sor in f:
                t = sor.split(';')
                
                # labdajatek;Labdajáték;nemdse;nem DSE;Ladányi Edina;Péntek;7:30;8:15;1;Nagy Szilvia;Péntek;14:30;15:15;10;22;
                # Tehát
                # [0]: labdajatek
                # [1]: Labdajáték
                # [2]: nemdse
                # [3]: nem DSE
                # [4]: Ladányi
                # [5]: Péntek
                # [6]: 7:30
                # [7]: 8:15
                # [8]: 1
                # [9]: Nagy Szilvia
                # [10]: Péntek
                # [11]: 14:30
                # [12]: 15:15
                # [13]: 10
                # [14]: 22
                #i+=1
                #print(f"{i}: foglalkozások beolvasásakor split kész")
                
                vanemasik = t[8]=='1'
                # beolvasott xx:xx alakú STRINGEK datetime-má alakítása, hogy aztán timedeltak legyenek, ami a durationfieldbe kell.
                et1 = datetime.strptime(t[6], "%H:%M")
                et2 = datetime.strptime(t[7], "%H:%M")
                mt1 = datetime.strptime(t[11], "%H:%M") if vanemasik else None
                mt2 = datetime.strptime(t[12], "%H:%M") if vanemasik else None
                #print(f"{i}: datetime konverziók készen")

                Foglalkozas.objects.create(
                    kod=t[0],
                    letszam=t[14],
                    tipus_kod=t[2],
                    tipus_nev=t[3],
                    nev=t[1],
                    egyik_nap=t[5],
                    egyik_mettol=timedelta(hours=et1.hour, minutes=et1.minute),
                    egyik_meddig=timedelta(hours=et2.hour, minutes=et2.minute),
                    egyik_tanar=t[4],
                    bomlik=vanemasik,
                    masik_nap=t[10] if vanemasik else None,
                    masik_mettol=timedelta(hours=mt1.hour, minutes=mt1.minute) if vanemasik else None,
                    masik_meddig=timedelta(hours=mt2.hour, minutes=mt2.minute) if vanemasik else None,
                    masik_tanar=t[9],
                )
                #print(f"{i}: foglalkozás készen")
             # end of for
        # end of with   
        print(f'{vezerlo.nev} vezérlő foglalkozásainak a beolvasása sikeres')
        #except:
        #    print(f'{vezerlo.nev} vezérlő usereinek a beolvasása sikertelen: beolvasáskor vagy a csoport lekérdezésekor valami félrement')
foglalkozasok_beolvasasa.short_description = "FOGLALKOZÁSOK feltöltése [vezerlo.kod]_foglalkozasinput.csv-ből"

def user_update(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        fajlnev = f"txt/emailek/{vezerlo.kod}.txt"

        
        if vezerlo.kod=='kulsos':
            for fh in Felhasznalo.objects.all():
                fh.kulsos = False
        elif vezerlo.kod=='gyogy':
            for fh in Felhasznalo.objects.all():
                fh.gyogy = False
        elif vezerlo.kod=='felmentett':
            for fh in Felhasznalo.objects.all():
                fh.felmentett = False


        with open(fajlnev, 'r', encoding="utf-8") as f:
            for sor_veggel in f:
                sor = sor_veggel.strip()

                kiakadt = False

                try:
                    a_user = User.objects.get(username=sor)
                except User.DoesNotExist:
                    print(f'--- !!! {sor} emaillel rendelkező user nincs a felhasználók között')
                    kiakadt = True

                try:
                    a_felhasznalo = Felhasznalo.objects.get(user=a_user)
                except Felhasznalo.DoesNotExist:
                    print(f'--- !!! {a_user}-hez nem tartozik felhasználó!')
                    kiakadt = True
                except UnboundLocalError:
                    kiakadt = True


                if not kiakadt:
                    if vezerlo.kod=='kulsos':
                        a_felhasznalo.kulsos = True
                    elif vezerlo.kod=='gyogy':
                        a_felhasznalo.gyogy = True
                    elif vezerlo.kod=='felmentett':
                        a_felhasznalo.felmentett = True
                    a_felhasznalo.save()
            # end of for f
        # end of with open
        print(f'{vezerlo.nev} vezérlő emailcímeivel sikerült frissíteni a felhasználói adatbázist')
    # end for queryset
user_update.short_description = f"UPDATE a külsős/gyógy-/felmentett tesisek [...].txt-ből"



def stop_jelentkezes(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        diakok_csoportja = Group.objects.get(name='diak')
        for user in filter(lambda u : diakok_csoportja in u.groups.all() and u.email!='molnar.attila@szlgbp.hu', User.objects.all()):
            user.is_active = False
            user.save()
    # end for queryset
stop_jelentkezes.short_description = f"STOP LOGIN"



def start_jelentkezes(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        diakok_csoportja = Group.objects.get(name='diak')
        for user in filter(lambda u : diakok_csoportja in u.groups.all() and u.email!='molnar.attila@szlgbp.hu', User.objects.all()):
            user.is_active = True
            user.save()
        pass
    # end for queryset
start_jelentkezes.short_description = f"START LOGIN"

def jelentkezesek_elkuldese(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        for a_foglalkozas in Foglalkozas.objects.all():
            print(levelkuldes_dir('molnar.attila@szlgbp.hu', [vezerlo.nev], 'emails/results', {'felhasznalok': a_foglalkozas.felhasznaloi(), 'cim': a_foglalkozas.nev},'debugszoveg:'))
    # end for queryset
jelentkezesek_elkuldese.short_description = f"EMAIL jelentkezések elküldése"

class VezerloAdmin(admin.ModelAdmin):
    actions = [
            userek_beolvasasa,
            foglalkozasok_beolvasasa,
            user_update,
            stop_jelentkezes,
            start_jelentkezes,
            jelentkezesek_elkuldese
        ]

admin.site.register(Vezerlo, VezerloAdmin)



def feljelentkezes_engedelyezese(modeladmin, request, queryset) -> None:
    for felhasznalo in queryset:
        felhasznalo.feljelentkezhet = True
        felhasznalo.save()
    # end for queryset
feljelentkezes_engedelyezese.short_description = f"feljelentkezés ON"

def lejelentkezes_engedelyezese(modeladmin, request, queryset) -> None:
    for felhasznalo in queryset:
        felhasznalo.lejelentkezhet = True
        felhasznalo.save()
    # end for queryset
lejelentkezes_engedelyezese.short_description = f"lejelentkezés ON"

def atjelentkezes_engedelyezese(modeladmin, request, queryset) -> None:
    for felhasznalo in queryset:
        felhasznalo.atjelentkezhet = True
        felhasznalo.save()
    # end for queryset
atjelentkezes_engedelyezese.short_description = f"atjelentkezés ON"

def feljelentkezes_tiltasa(modeladmin, request, queryset) -> None:
    for felhasznalo in queryset:
        felhasznalo.feljelentkezhet = False
        felhasznalo.save()
    # end for queryset
feljelentkezes_tiltasa.short_description = f"feljelentkezés OFF"

def lejelentkezes_tiltasa(modeladmin, request, queryset) -> None:
    for felhasznalo in queryset:
        felhasznalo.lejelentkezhet = False
        felhasznalo.save()
    # end for queryset
lejelentkezes_tiltasa.short_description = f"lejelentkezés OFF"

def atjelentkezes_tiltasa(modeladmin, request, queryset) -> None:
    for felhasznalo in queryset:
        felhasznalo.atjelentkezhet = False
        felhasznalo.save()
    # end for queryset
atjelentkezes_tiltasa.short_description = f"atjelentkezés OFF"



class FelhasznaloAdmin(admin.ModelAdmin):
    actions = [
        feljelentkezes_engedelyezese,
        lejelentkezes_engedelyezese,
        atjelentkezes_engedelyezese,
        feljelentkezes_tiltasa,
        lejelentkezes_tiltasa,
        atjelentkezes_tiltasa,
        ]

admin.site.register(Felhasznalo, FelhasznaloAdmin)

# - Foglalkozások beolvasása?
# - Osztály léptetése