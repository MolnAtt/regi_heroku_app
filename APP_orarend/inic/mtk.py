from APP_orarend.inic.csv2table import csv2table
from APP_orarend.models import MTK, Tanar, Munkakozosseg

csv2table(MTK, "APP_orarend/inic/csvs/mtk.csv", [
    {
        'tabla': Tanar, 
        'idegen_kulcs': 'tanar',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Munkakozosseg, 
        'idegen_kulcs': 'munkakozosseg',
        'tabla_kulcs': 'nev'
    },
])
