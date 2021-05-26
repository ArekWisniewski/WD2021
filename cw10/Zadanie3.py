# Na jednym wykresie wygeneruj wykresy funkcji sin(x) oraz cos(x) dla x ϵ [0, 30] z krokiem 0.1.
# Dodaj etykiety i legendę do wykresu.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,30,0.1)
s=np.sin(x)
c=np.cos(x)
plt.plot(x,s, label='sin(x)')
plt.plot(x,c, label='cos(x)')
plt.legend()
plt.show()