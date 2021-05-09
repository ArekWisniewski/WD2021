# Wczytaj plik  /datasets/zamowieniana.csv a następnie wyświetl:
# - listę unikalnych nazwisk sprzedawców (przetwarzając zwróconą pojedynczą kolumnę z DataFrame)
# - 5 najwyższych wartości zamówień
# - ilość zamówień złożonych przez każdego sprzedawcę
# - sumę zamówień dla każdego kraju
# - sumę zamówień dla roku 2005, dla sprzedawców z Polski
# - średnią kwotę zamówienia w 2004 roku,
# - zapisz dane za 2004 rok do pliku zamówienia_2004.csv a dane za 2005 do pliku zamówienia_2005.csv

import pandas as pd


odczyt = pd.read_csv('zamowienia.csv', header=0, delimiter=';')
#3a
print(odczyt['Sprzedawca'].unique())
#3b
max=odczyt.sort_values('Utarg', ascending = False).iloc[[0,1,2,3,4]]
print(max['Utarg'])
#3c
ilosc=odczyt.groupby(['Sprzedawca']).count()
print(ilosc['idZamowienia'])
#3d
print(odczyt.groupby(odczyt['Kraj']).agg({'idZamowienia':['count']}))
#3e
rokpl = odczyt[(odczyt['Data zamowienia'] >= '2005-01-01') & (odczyt['Data zamowienia'] <= '2005-12-31') & (odczyt['Kraj']=='Polska')].groupby(['Kraj']).count()
print(rokpl['idZamowienia'])
#3f
sr = odczyt[(odczyt['Data zamowienia'] >= '2004-01-01') & (odczyt['Data zamowienia'] <= '2004-12-31')].mean()
print(sr['Utarg'])
#3g
cztery = odczyt[(odczyt['Data zamowienia'] >= '2004-01-01') & (odczyt['Data zamowienia'] <= '2004-12-31')]
piec = odczyt[(odczyt['Data zamowienia'] >= '2005-01-01') & (odczyt['Data zamowienia'] <= '2005-12-31')]
cztery.to_csv('zamowienia_2004.csv', header=None)
piec.to_csv('zamowienia_2005.csv', header=None)