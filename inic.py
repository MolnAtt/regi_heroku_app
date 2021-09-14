from APP.models import Vezerlo, Osztaly
from django.contrib.auth.models import User, Group

Group.objects.get_or_create(name='testnevelotanar')[0] 
Group.objects.get_or_create(name='adminisztrator')[0]  
Group.objects.get_or_create(name='diak')[0] 

Vezerlo.objects.get_or_create(kod="2021_osz", nev="2021 őszi jelentkezés")

print("inic.py lefutott, mindenhol get_or_create volt, szóval nem termelődtek duplikátumok")
