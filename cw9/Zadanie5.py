# Wyświetl na pomocą wykresu słupkowego ilość złożonych zamówień przez poszczególnych sprzedawców (zbiór danych zamówienia.csv).

import pandas as pd
import matplotlib.pyplot as plt

odczyt = pd.read_csv('zamowienia.csv', header=0, delimiter=';')
grupa = odczyt.groupby(['Sprzedawca']).count()
grupa = grupa['idZamowienia']
wykres = grupa.plot.bar()
plt.show()