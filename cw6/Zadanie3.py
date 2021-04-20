# Napisz funkcję, która będzie:
# - przyjmowała jeden parametr ‘n’ w postaci liczby całkowitej
# - zwracała tablicę Numpy o wymiarach n*n kolejnych liczb całkowitych poczynając od 1

import numpy as np
def macierz(n):
    m = np.array(n*[np.arange(n)])
    print(m)
macierz(5)