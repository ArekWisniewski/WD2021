# Utwórz macierz 3x3 oraz 4x4 i znajdź najniższe wartości dla każdej kolumny i każdego rzędu.

import numpy as np

a=np.arange(9).reshape(3, 3)
b=np.arange(16).reshape(4, 4)

print(a)
print(b)
print(a.min(axis=1))
print(b.min(axis=1))
print(a.min(axis=0))
print(b.min(axis=0))