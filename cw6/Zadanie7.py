# Napisz funkcję, która wygeneruje macierz wielowymiarową postaci:
# [[2 4 6]
#  [4 2 4]
#  [6 4 2]]
# Przy założeniach:
# - funkcja przyjmuje parametr n, który określa wymiary macierzy jako n*n i umieszcza wielokrotność liczby 2
# na kolejnych jej przekątnych rozchodzących się od głównej przekątnej.

import numpy as np

def generuj(n):
    tab=np.diag([2 for a in range(n)])
    for i in range(1, n):
        a=np.diag([2*(i+1) for a in range(n-i)],+i)
        b=np.diag([2*(i+1) for a in range(n-i)],-i)
        tab=tab+a+b
    return tab

print(generuj(5))