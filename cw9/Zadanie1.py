# Stwórz wykres liniowy, który wyświetli liczbę urodzonych dzieci dla każdego roku.

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
odczyt = pd.read_excel(plik)
grupa = odczyt.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.plot(xticks=grupa.index.values)
plt.show()
