print('------ all.py indul')

from django.contrib.auth.models import Group

"""  létfontosságú csoportok feldolgozása  """

Group.objects.get_or_create(name='adminisztrator')[0]  
Group.objects.get_or_create(name='latogato')[0] 

print("--- all.py: létfontosságú csoportok létrejöttek")

""" csv fájlok feldolgozása """

import APP_orarend.inic.nap
import APP_orarend.inic.tantargy
import APP_orarend.inic.szarny
import APP_orarend.inic.terem
import APP_orarend.inic.tanar
import APP_orarend.inic.munkakozosseg
import APP_orarend.inic.mtk
import APP_orarend.inic.osztaly
import APP_orarend.inic.csoport
import APP_orarend.inic.csok
import APP_orarend.inic.ora

print("--- all.py: csv-fájlok alapján elkészült az adatbázis")

print("------ all.py befejeződött")

