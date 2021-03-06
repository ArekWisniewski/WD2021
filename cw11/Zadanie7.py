# Połącz 2 wykresy z zadania 5 w jeden. Odpowiednio formatując wykresy spróbuj osiągnąć efekt
# jakby była to gra Snake, w której zielony wąż próbuje zjeść czerwone jabłka.

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


def randrange(n, vmin, vmax):
    return (vmax - vmin) * np.random.rand(n) + vmin


fig = plt.figure()
ax = fig.gca(projection="3d")
n = 20

for c, m, zlow, zhigh in [("r", "o", -5, 5)]:
    xs = randrange(n, 23, 32)
    ys = randrange(n, 0, 0)
    zs = randrange(n, zlow, zhigh)
    ax.scatter(xs, ys, zs, c=c, marker=m, label="Jabłka")

ax = fig.gca(projection="3d")
t = np.linspace(0, 2 * np.pi, 5)
z = t
x = np.sin(t) - 1
y = np.cos(t) * 0
ax.plot(x + 30, y, z, label="Wąż", color="g", linewidth=4)
ax.legend()
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.view_init(elev=0., azim=-90)
ax.set_facecolor('black')
fig.patch.set_facecolor('black')
plt.axis('off')
ax.grid(False)
plt.show()