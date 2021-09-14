from APP.models import Vezerlo, Osztaly
from django.contrib.auth.models import User, Group

Group.objects.get_or_create(name='testnevelotanar')[0] 
Group.objects.get_or_create(name='adminisztrator')[0]  
Group.objects.get_or_create(name='diak')[0] 

Vezerlo.objects.get_or_create(kod="2021_osz", nev="Foglalkozáslista: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_kny", nev="KNY: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_nye", nev="NYE: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_nyf", nev="NYF: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_9a", nev="9A: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_9b", nev="9B: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_9c", nev="9C: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_9d", nev="9D: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_9e", nev="9D: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_9f", nev="9F: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_10a", nev="10A: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_10b", nev="10B: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_10c", nev="10C: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_10d", nev="10D: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_10e", nev="10E: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_10f", nev="10F: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_11a", nev="11A: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_11b", nev="11B: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_11d", nev="11D: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_11e", nev="11E: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_11f", nev="11F: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_12a", nev="12A: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_12b", nev="12B: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_12d", nev="12D: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_12e", nev="12E: 2021 őszi jelentkezés")
Vezerlo.objects.get_or_create(kod="2021_osz_12f", nev="12F: 2021 őszi jelentkezés")

print("inic.py lefutott, mindenhol get_or_create volt, szóval nem termelődtek duplikátumok")
