from django.contrib import admin

from .models import Nap, Jelentkezes, Felhasznalo, Osztaly, Tipus, Foglalkozas

admin.site.register(Nap)
admin.site.register(Jelentkezes)
admin.site.register(Felhasznalo)
admin.site.register(Tipus)
admin.site.register(Foglalkozas)
admin.site.register(Osztaly)

# a trükkös admin-funkciókról, függvényekről az szlgbp_ma_heroku gitrepoban vannak jó példák.


# metódusok, amelyekre szükség van: 
# - Felhasználók beolvasása

# - Foglalkozások beolvasása?
# - Osztály léptetése