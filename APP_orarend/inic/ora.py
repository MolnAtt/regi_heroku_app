from APP_orarend.inic.csv2table import csv2table
from APP_orarend.models import Ora, Nap, Csoport, Tantargy, Tanar, Terem

csv2table(Ora, "APP_orarend/inic/csvs/ora.csv", [
    {
        'tabla': Nap, 
        'idegen_kulcs': 'nap',
        'tabla_kulcs': 'sorszam'
    },
    {
        'tabla': Csoport, 
        'idegen_kulcs': 'csoport',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Tantargy, 
        'idegen_kulcs': 'tantargy',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Tanar, 
        'idegen_kulcs': 'tanar',
        'tabla_kulcs': 'kreta'
    },
    {
        'tabla': Terem, 
        'idegen_kulcs': 'terem',
        'tabla_kulcs': 'kreta'
    },
])
