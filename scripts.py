from django.contrib.auth.models import User, Group

# osztalyok=[ 'kny', 'nye', 'nyf', '9a', '9b', '9c', '9d', '9e', '9f', '10a', '10b', '10c', '10d', '10e', '10f', '11a', '11b', '11d', '11e', '11f', '12a', '12b', '12d', '12e', '12f']
osztalyok=[ '17a', '17e', '17f', '18a', '18b', '18d', '18e', '18f', '19a', '19b', '19d', '19e', '19f', '20a', '20b', '20c', '20d', '20e', '20f', '21a', '21b', '21c', '21d', '21e', '21f']

targy = 'Bejelentkezési adatok a testnevelés foglalkozások választásához'

for osztaly in osztalyok:
    honnan = f"txt/userek/{osztaly}_userinput.csv"
    hova = f"txt/emailek/{osztaly}_email.csv"
    with open(honnan, 'r', encoding="utf-8") as f:
        with open(hova, 'w', encoding="utf-8") as g:
            g.write('targy;'+f.readline())
            for sor in f:
                g.write(targy + ';' + sor)
    print(f'{osztaly} csv-je kész')

print(f'összes csv-je kész')



