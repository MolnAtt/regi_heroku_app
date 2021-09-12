from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Nap, Jelentkezes, Felhasznalo, Osztaly, Tipus, Foglalkozas, Vezerlo

admin.site.register(Nap)
admin.site.register(Jelentkezes)
admin.site.register(Felhasznalo)
admin.site.register(Tipus)
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
userek_beolvasasa.short_description = "felhasználók feltöltése [feladatcsoport.code]_userinput.csv-ből"


class VezerloAdmin(admin.ModelAdmin):
    actions = [
            userek_beolvasasa,
        ]

admin.site.register(Vezerlo, VezerloAdmin)


# - Foglalkozások beolvasása?
# - Osztály léptetése