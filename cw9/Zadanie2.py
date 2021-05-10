# Stwórz wykres słupkowy, który wyświetli liczbę urodzonych chłopców i dziewczynek z całego zbioru.

import pandas as pd
import matplotlib.pyplot as plt
import xlrd
import openpyxl

df = pd.read_excel(pd.ExcelFile("imiona.xlsx"), "Arkusz1")
p = df.groupby(['Plec']).agg({"Liczba": ["sum"]})
plt.ylabel('Ilość urodzeń (mln)')
plt.xlabel('Płeć')
plt.bar(['K', 'M'], [p.values[0][0], p.values[1][0]])
plt.show()