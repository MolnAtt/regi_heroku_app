from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Jelentkezes, Felhasznalo, Osztaly, Foglalkozas, Vezerlo
from datetime import datetime, timedelta


admin.site.register(Jelentkezes)
admin.site.register(Felhasznalo)
admin.site.register(Foglalkozas)
admin.site.register(Osztaly)

# a trükkös admin-funkciókról, függvényekről az szlgbp_ma_heroku gitrepoban vannak jó példák.


# metódusok, amelyekre szükség van: 
# - Felhasználók beolvasása


def userek_beolvasasa(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        #try:
        fajlnev = f"txt/userek/{vezerlo.kod}_userinput.csv"

        with open(fajlnev, 'r', encoding="utf-8") as f:
            for sor in f:
                sortomb = sor.split(';')
                
                # Tóth Dóra;tothdora;21f;toth.dora.21f@szlgbp.hu;ertdfgcvb
                # Tehát
                # [0]: Tóth Dóra;
                # [1]: tothdora;
                # [2]: 21f;
                # [3]: toth.dora.21f@szlgbp.hu;
                # [4]: qwerasdf
                
                
                a_csoport = Group.objects.get_or_create(name=sortomb[2])[0]  # mert (Group, bool) alakban ad vissza a get_or_create!
                az_osztaly = Osztaly.objects.get_or_create(kod=sortomb[2])[0]
                
                a_user = User.objects.create(
                    username=sortomb[1], 
                    email=sortomb[3],
                    password=sortomb[4],
                    )

                Felhasznalo.objects.create(
                    nev=sortomb[0],
                    user=a_user,
                    osztaly=az_osztaly,
                    )

                a_user.groups.add(a_csoport)
        print(f'{vezerlo.nev} vezérlő usereinek a beolvasása sikeres')
        #except:
        #    print(f'{vezerlo.nev} vezérlő usereinek a beolvasása sikertelen: beolvasáskor vagy a csoport lekérdezésekor valami félrement')
userek_beolvasasa.short_description = "felhasználók feltöltése [vezerlo.kod]_userinput.csv-ből"

def foglalkozasok_beolvasasa(modeladmin, request, queryset) -> None:
    for vezerlo in queryset:
        #try:
        fajlnev = f"txt/foglalkozasok/{vezerlo.kod}_foglalkozasinput.csv"

        with open(fajlnev, 'r', encoding="utf-8") as f:
            i=0
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
                i+=1
                print(f"{i}: foglalkozások beolvasásakor split kész")
                
                vanemasik = t[8]=='1'
                # beolvasott xx:xx alakú STRINGEK datetime-má alakítása, hogy aztán timedeltak legyenek, ami a durationfieldbe kell.
                et1 = datetime.strptime(t[6], "%H:%M")
                et2 = datetime.strptime(t[7], "%H:%M")
                mt1 = datetime.strptime(t[11], "%H:%M") if vanemasik else None
                mt2 = datetime.strptime(t[12], "%H:%M") if vanemasik else None
                print(f"{i}: datetime konverziók készen")

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
                print(f"{i}: foglalkozás készen")
             # end of for
        # end of with   
        print(f'{vezerlo.nev} vezérlő usereinek a beolvasása sikeres')
        #except:
        #    print(f'{vezerlo.nev} vezérlő usereinek a beolvasása sikertelen: beolvasáskor vagy a csoport lekérdezésekor valami félrement')
foglalkozasok_beolvasasa.short_description = "foglalkozások feltöltése [vezerlo.kod]_foglalkozasinput.csv-ből"


class VezerloAdmin(admin.ModelAdmin):
    actions = [
            userek_beolvasasa,
            foglalkozasok_beolvasasa,
        ]

admin.site.register(Vezerlo, VezerloAdmin)


# - Foglalkozások beolvasása?
# - Osztály léptetése