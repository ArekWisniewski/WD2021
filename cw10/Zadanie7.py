# Korzystając z tutoriala pod adresem https://towardsdatascience.com/matplotlib-tutorial-learn-basics-of-pythons-powerful-plotting-library-b5d1b8f67596
# lub innego zmodyfikuj wykres 2 z zadania 6 tak, aby zamiast wykresu liniowego przedstawiał wykres słupkowy skumulowany
# (czyli jeden słupek dla kobiet i mężczyzn, ale składający się z dwóch „nałożonych” na siebie słupków).

import pandas as pd
import xlrd
import openpyxl
import matplotlib.pyplot as plt

df = pd.read_excel(pd.ExcelFile("imiona.xlsx"), "Arkusz1")
m = df[df["Plec"] == 'M'].groupby(['Rok']).sum()
k = df[df["Plec"] == 'K'].groupby(['Rok']).sum()
plt.bar(df.Rok.unique(), [m.values[y][0] for y in range(len(m.values))], color="blue", label="M")
plt.bar(df.Rok.unique(), [k.values[y][0] for y in range(len(k.values))], color="pink", label="K", bottom=[m.values[y][0] for y in range(len(m.values))])
plt.xticks(df.Rok.unique(), rotation=60)
plt.ylabel('Ilość urodzeń')
plt.xlabel('Rok')
plt.legend()
plt.show()