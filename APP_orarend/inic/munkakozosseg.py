from APP_orarend.inic.csv2table import csv2table
from APP_orarend.models import Munkakozosseg

csv2table(Munkakozosseg, "APP_orarend/inic/csvs/munkakozosseg.csv")
