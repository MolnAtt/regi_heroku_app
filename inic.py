print('------ inic.py indul')

from APP.models import Vezerlo, Osztaly
from django.contrib.auth.models import User, Group


"""  létfontosságú csoportok feldolgozása  """

Group.objects.get_or_create(name='testnevelotanar')[0] 
Group.objects.get_or_create(name='adminisztrator')[0]  
Group.objects.get_or_create(name='diak')[0] 

print("--- inic.py: létfontosságú csoportok létrejöttek")


"""  allusers.csv feldolgozása  """

fajlnev = f"txt/userek/allusers.csv" # csv feltétlen tartalmazza az (ékezetmentes stb.?) mezőneveket!
mezonevek_sora=''
with open(fajlnev, 'r', encoding="utf-8") as f:
    mezonevek_sora = f.readline()
    mezonevek = mezonevek_sora.strip().split(';')+['sor']
    rekordok = list(map(lambda sor : dict(zip(mezonevek, sor.strip().split(';')+[sor])), f))
    
osztalykodok = set(map(lambda rekord: rekord['osztalykod'], rekordok))
for kod in osztalykodok:
    with open(f'txt/userek/{kod}_userinput.csv', 'w', encoding='utf8') as f:
        f.write(mezonevek_sora)
        for sor in map( lambda r: r['sor'], filter(lambda rekord : rekord['osztalykod']==kod, rekordok)):
            f.write(sor)

print("--- inic.py: allusers.csv szétdobva osztálykódonként külön userinput.csv-kre")

""" Vezérlők elkészítése """

Vezerlo.objects.get_or_create(kod="2021_osz", nev="Foglalkozáslista: 2021 őszi jelentkezés")
print("--- inic.py: 2021_osz_foglalkozasinput.csv-t beolvasó Vezérlő elkészült")

Vezerlo.objects.get_or_create(kod="kulsos", nev="Külsős diákok listája")
print("--- inic.py: kulsos_update.txt-t beolvasó Vezérlő elkészült")

Vezerlo.objects.get_or_create(kod="gyogy", nev="Gyógytesis diákok listája")
print("--- inic.py: gyogy_update.txt-t beolvasó Vezérlő elkészült")

Vezerlo.objects.get_or_create(kod="felmentett", nev="Felmentett diákok listája")
print("--- inic.py: felmentett_update.txt-t beolvasó Vezérlő elkészült")

Vezerlo.objects.get_or_create(kod="jelentkezesvezerlo", nev="0")
print("--- inic.py: jelentkezésvezértlő elkészült")

Vezerlo.objects.get_or_create(kod="email_target", nev="molnar.attila@szlgbp.hu")
print("--- inic.py: emailküldő (default-target: molnar.attila@szlgbp.hu) elkészült")

Vezerlo.objects.get_or_create(kod="karbantartasjelzes", nev="0")
print("--- inic.py: karbantartásjelző elkészült")



for a_kod in osztalykodok:
    Vezerlo.objects.get_or_create(kod=a_kod, nev=f"{a_kod}: 2021 őszi jelentkezés")

print("--- inic.py: userinput.csv-ket beolvasó Vezérlők elkészültek")
print("------ inic.py befejeződött")




