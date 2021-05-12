# Wykres kołowy z wartościami % ukazującymi ilość urodzonych chłopców i dziewczynek w ostatnich 5 latach z datasetu.

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik, 'Arkusz1')
grupa = dane['Rok'].max()
wykres = dane[dane['Rok'] >= 2013].groupby(['Plec']).agg({'Liczba': ['sum']})
wykres.plot.pie(subplots=True, autopct='%.2f%%', fontsize=20)
plt.show()