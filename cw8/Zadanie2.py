# Zadanie 2
# Z danych z zadania 1 wyświetl (korzystając w miarę możliwości z funkcji biblioteki Pandas):
# - tylko te rekordy gdzie liczba nadanych imion była większa niż 1000 w danym roku
# - tylko rekordy gdzie nadane imię jest takie jak Twoje
# - sumę wszystkich urodzonych dzieci w całym danym okresie,
# - sumę dzieci urodzonych w latach 2000-2005
# - sumę urodzonych chłopców i dziewczynek,
# - najbardziej popularne imię dziewczynki i chłopca w danym roku ( czyli po 2 rekordy na rok),
# - najbardziej popularne imię dziewczynki i chłopca w całym danym okresie,

import numpy as np
import pandas as pd

plik=pd.ExcelFile('imiona.xlsx')
a=pd.read_excel(plik,'Arkusz1')
#2a
print(a[a['Liczba']>1000])
#2b
print(a[a['Imie']=='ARKADIUSZ'])
#2c
print(a['Liczba'].sum())
#2d
print(a.loc[((a.Rok > 1999) & (a.Rok < 2006)), ['Liczba']].sum())
#2e
print(a.groupby(a['Plec']).agg({'Liczba':['sum']}))
#2f
print(a.sort_values('Liczba', ascending=False).groupby(['Rok', 'Plec']).nth(0))
#2g
print(a.groupby(['Plec','Imie']).agg({'Liczba':['sum']}).sort_values(('Liczba','sum'), ascending = False).iloc[[0,1]])