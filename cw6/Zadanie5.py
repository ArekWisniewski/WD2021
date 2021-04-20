# Napisz funkcję, która:
# - na wejściu przyjmuje jeden parametr określający długość wektora,
# - na podstawie parametru generuje wektor, ale w kolejności odwróconej (czyli np. dla n=3 =>[3 2 1])
# - generuje macierz diagonalną z w/w wektorem jako przekątną

import numpy as np

def wektor(x):
    w=np.diag([n for n in range(x, 0, -1)])
    return w

print(wektor(6))