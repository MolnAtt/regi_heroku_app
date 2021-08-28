from django.contrib import admin

from .models import Nap, Jelentkezes, Felhasznalo, Tipus, Foglalkozas

admin.site.register(Nap)
admin.site.register(Jelentkezes)
admin.site.register(Felhasznalo)
admin.site.register(Tipus)
admin.site.register(Foglalkozas)

# a trükkös admin-funkciókról, függvényekről az szlgbp_ma_heroku gitrepoban vannak jó példák.
