# Wygeneruj wykres punktowy dla 5 różnych losowych serii z użyciem różnych znaczników i
# kolorów: https://matplotlib.org/api/markers_api.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import random

markery = [',', '.', 'o', 'v', '^', '>', '<', '1', '2', '3', '4', '8', 's', 'p', 'P', '*', 'h', 'H', 'x', 'X', '+', 'd',
           'D']
kolory = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'w']


def randrange(n, vmin, vmax):
    wynik = np.random.rand(n) * (vmax - vmin) + vmin
    return wynik


fig = plt.figure()
ax = fig.gca(projection='3d')

for a in range(5):
    c = kolory[np.random.randint(len(kolory))]
    marker = markery[np.random.randint(len(markery))]
    x = randrange(100, 0, 100)
    y = randrange(100, 0, 150)
    z = randrange(100, 0, 200)
    ax.scatter(x, y, z, c=c, marker=marker)

plt.show()