# Wygeneruj macierz płaską i przekształć ja na 3x4.
# Wygeneruj w ten sposób jeszcze kombinacje 4x3 i 2x6.
# Spłaszcz każdą z nich i wyświetl wyniki. Czy są identyczne?

import numpy as np

a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)
c = np.arange(12).reshape(2, 6)
a1=a.ravel()
b1=b.ravel()
c1=c.ravel()
print(a1)
print(b1)
print(c1)