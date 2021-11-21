from APP_orarend.inic.csv2table import csv2table
from APP_orarend.models import CSOK, Csoport, Osztaly

csv2table(CSOK, "APP_orarend/inic/csvs/csok.csv", [
    {
        'tabla': Csoport, 
        'idegen_kulcs': 'csoport',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Osztaly, 
        'idegen_kulcs': 'osztaly',
        'tabla_kulcs': 'kreta'
    },
])