# Wczytaj do DataFrame arkusz z narodzinami dzieci w Polsce dostępny pod adresem /datasets/imiona.xlsx

import numpy as np
import pandas as pd
import xlrd
import openpyx1

plik = pd.ExcelFile('imiona.xlsx')
odczyt = pd.read_excel(plik, 'Arkusz1')
print(odczyt.sample())
