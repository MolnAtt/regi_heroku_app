def csv2dictlistreversible(fajlnev):
    mezonevek_sora=''
    with open(fajlnev, 'r', encoding="utf-8") as f:
        mezonevek_sora = f.readline()
        mezonevek = mezonevek_sora.strip().split(',')+['sor']
        return list(map(lambda sor : dict(zip(mezonevek, sor.strip().split(',')+[sor])), f))

def csv2dictlist(csvpath):
    mezonevek_sora=''
    with open(csvpath, 'r', encoding="utf-8") as f:
        mezonevek_sora = f.readline()  
        mezonevek = mezonevek_sora.strip().split(',')
        return list(map(lambda sor : dict(zip(mezonevek, sor.strip().split(','))), f))

def csv2table(osztaly, csvpath, kapcsolatok=[]): # csv feltétlen tartalmazza az (ékezetmentes stb.?) mezőneveket, amelyek megegyeznek a tábla mezőneveivel!
    for rekord in csv2dictlist(csvpath):
        for kapcsolat in kapcsolatok:
            kwargs = {kapcsolat['tabla_kulcs']:rekord[kapcsolat['idegen_kulcs']]}
            try:
                rekord[kapcsolat['idegen_kulcs']] = kapcsolat['tabla'].objects.get(**kwargs)
            except:
                print(f'az idegenkulcs kapcsolása (objects.get) nem működött: ')
                print(f'rekord[{kapcsolat["idegen_kulcs"]}] = {kapcsolat["tabla"]}.objects.get({kwargs}) ')
                print(f'valószínűleg ezért:')
                print(f'rekord[kapcsolat["idegen_kulcs"]]={rekord[kapcsolat["idegen_kulcs"]]}')
                raise Exception("Tehát nem stimmelnek a kulcsok!!!")
                
        osztaly.objects.get_or_create(**rekord)
    print(f"--- inic.py: {csvpath} fájl adattáblává alakítva")
