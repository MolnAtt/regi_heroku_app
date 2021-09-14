from APP.models import Vezerlo

print("fut az inic.py, ennyi vezérlő van:")
print(Vezerlo.objects.all().count())

""" innen lehet copyzni

    Vezerlo.objects.create(kod="", nev="")

"""

Vezerlo.objects.create(kod="2021_osz", nev="2021 őszi jelentkezés")
