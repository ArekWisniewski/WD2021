# Wygeneruj macierz 3x3 i wyświetl w pętli każdy z rzędów.

import numpy as np

m = np.arange(9).reshape(3,3)
for i in m:
   print(i)