# Wygeneruj macierz 9x9 a następnie zmień jej kształt. Jakie mamy możliwości i dlaczego(kolumny*wiersze==elementy)?

import numpy as np

a = np.arange(81).reshape(9,9)
print(a)
b = a.ravel()
print(b)
c = a.reshape(1,81)
print(c)
d = a.reshape(3,27)
print(d)
e=a.reshape(27,3)
print(e)
f=a.reshape(81,1)
print(f)