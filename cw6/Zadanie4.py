# Napisz funkcję, która będzie przyjmowała 2 parametry: liczbę, która będzie podstawą operacji potęgowania oraz ilość kolejnych potęg do wygenerowania.
# Korzystając z funkcji logspace generuj tablicę jednowymiarową kolejnych potęg podanej liczby, np. generuj(2,4) -> [2 4 8 16]

import numpy as np

def potegowanie(podstawa,ilosc):
    return np.logspace(1.0, ilosc, num=ilosc, base = podstawa, dtype=int)

print(potegowanie(2,4))