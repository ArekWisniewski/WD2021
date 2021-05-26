# Napisz funkcję, która losowo rzuca dwiema kostkami k6 n razy. Wynik rzutów zapisywany jest w postaci listy
# sum oczek z tych dwóch kostek.
# Np. rzucaj(6) generuje 6 rzutów kostkami i zwraca wektor 6 sum oczek każdego rzutu. Po zakończeniu funkcji
# wyświetlaj histogram sumy rzutów. Dodaj stosowne etykiety do wykresu.

import numpy as np
import random as rng
import matplotlib.pyplot as plt

def rzucaj(n):
    k=0
    sumy=[]
    while(k<n):
        a = rng.randint(1,6)+rng.randint(1,6)
        sumy.append(a)
        k+=1
    return sumy

lista=rzucaj(1000)
plt.hist(lista, bins=11, facecolor="red", alpha=0.75)
plt.xlabel('Wartości')
plt.ylabel('Ilość rzutów o danej sumie')
plt.title('Histogram')
plt.grid(True)
plt.show()