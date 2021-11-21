from APP_orarend.inic.csv2table import csv2table
from APP_orarend.models import Nap

csv2table(Nap, "APP_orarend/inic/csvs/nap.csv")