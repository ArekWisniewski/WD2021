# Wygeneruj z pomocą dokumentacji wykres słupkowy z przykładu 4 wykorzystując 5 różnych kombinacji wyglądu.

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

kolory = ["m", "b", "r", "g", "y"]
fig = plt.figure(figsize=(8, 3))

for color_index in range(1, 6):
    ax = fig.add_subplot(2, 3, color_index, projection='3d')
    ax = fig.gca(projection="3d")
    _x = np.arange(4)
    _y = np.arange(5)
    _xx, _yy = np.meshgrid(_x, _y)
    x, y = _xx.ravel(), _yy.ravel()
    top = x + y
    bottom = np.zeros_like(top)
    width = depth = 1
    ax.bar3d(x, y, bottom, width, depth, top, shade=True, color=kolory[color_index - 1])
    if (color_index == 2):
        ax.set_title("Wykresy słupkowe zacieniowane")
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
plt.show()