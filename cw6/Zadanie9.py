# Wykorzystaj poznane na zajęciach funkcje biblioteki Numpy i stwórz macierz 5x5, która będzie zawierała kolejne wartości ciągu Fibonacciego.

import numpy as np

fib = np.arange(25)
fib[0] = 0
fib[1] = 1
for x in range(2, 25):
    fib[x] = fib[x - 1] + fib[x - 2]

fib = fib.reshape((5, 5))
print(fib)