# Korzystając z biblioteki pandas wczytaj zbiór danych z narodzinami dzieci przedstawiony w lekcji 8.
# Następnie na jednym płótnie wyświetl 3 wykresy
# (jeden wiersz i 3 kolumny). Dodaj do wykresów stosowne etykiety. Poustawiaj różne kolory dla wykresów.
# 1 wykres – wykres słupkowy przedstawiający ilość narodzonych dziewczynek i chłopców w całym okresie.
# 2 wykres – wykres liniowy, gdzie będą dwie linie, jedna dla ilości urodzonych kobiet, druga dla mężczyzn
# dla każdego roku z osobna.
# Czyli y to ilość narodzonych kobiet lub mężczyzn (dwie linie), x to rok.
# 3 wykres – wykres słupkowy przedstawiający sumę urodzonych dzieci w każdym roku.

import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("imiona.xlsx"), "Arkusz1")
p = df.groupby(['Plec']).agg({"Liczba": ["sum"]})
m = df[df["Plec"] == 'M'].groupby(['Rok']).sum()
k = df[df["Plec"] == 'K'].groupby(['Rok']).sum()
d = df.groupby(['Rok']).agg({"Liczba": ["sum"]})

plt.subplot(1, 3, 1)
plt.bar(['K', 'M'], [p.values[0][0], p.values[1][0]], color=['pink', 'blue'])
plt.ylabel('Ilość urodzeń (mln)')
plt.xlabel('Płeć')
plt.subplot(1, 3, 2)
plt.plot(df.Rok.unique(), [m.values[y][0] for y in range(len(m.values))], "y", label="M")
plt.plot(df.Rok.unique(), [k.values[y][0] for y in range(len(k.values))], "m", label="K")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend()
plt.subplot(1, 3, 3)
plt.bar(df.Rok.unique(), [d.values[y][0] for y in range(len(d.values))], color="green")
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.show()