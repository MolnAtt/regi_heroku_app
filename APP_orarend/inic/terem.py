from APP_orarend.inic.csv2table import csv2table
from APP_orarend.models import Terem, Szarny


csv2table(Terem, "APP_orarend/inic/csvs/terem.csv", [
    {
        'tabla': Szarny, 
        'idegen_kulcs': 'szarny',
        'tabla_kulcs': 'hosszu'
    },
])