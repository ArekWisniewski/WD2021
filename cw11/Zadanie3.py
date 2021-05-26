# Wygeneruj wykres z przykładu 3 w 5 różnych kolorystkach: https://matplotlib.org/examples/color/colormaps_reference.html

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

kolory = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd',
          'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']
fig = plt.figure()
for x in range(5):
    mapa = np.random.randint(len(kolory))
    ax = fig.add_subplot(3, 2, x + 1, projection='3d')
    X = np.arange(- 5, 5, 0.25)
    Y = np.arange(- 5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X ** 2 + Y ** 2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, cmap=kolory[mapa], linewidth=0, antialiased=False)
    ax.set_zlim(- 1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(2))
    fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()