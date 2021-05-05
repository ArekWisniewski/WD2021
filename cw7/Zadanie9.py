# Wygeneruj macierz 3x3 i wyświetl w pętli każdy element korzystając z opcji “spłaszczenia” macierzy.

import numpy as np

a=np.arange(9).reshape(3,3)
for i in a.ravel():
    print(i)