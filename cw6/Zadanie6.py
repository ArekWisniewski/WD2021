# Stwórz skrypt który na wyjściu wyświetli macierz numpy (tablica wielowymiarowa) w postaci wykreślanki,
# gdzie jedno słowo będzie wypisane w kolumnie, jedno w wierszu i jedno po ukosie.
# Jedno z tych słów powinno być wypisane od prawej do lewej.

import numpy as np
n1="wyraz"
n2="wazon"
n3="wujek"
m1 = np.array(list(n1))
m2 = np.array(list(n2))
m3 = np.diag(list(n3))
m3[:,0]=m1
m3[0:1]=m2
print(m3)