# Na wykresie wyświetl wykres liniowy funkcji f(x) = 1/x dla x ϵ [1, 20].Dodaj etykietę do linii wykresu i wyświetl legendę.
# Dodaj odpowiednie etykiety do osi wykresu (‘x’, ’f(x)’) oraz ustaw zakres osi na (0, 1) oraz (1, długość wektora x).

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,21)
plt.plot(x, 1/x, label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0,len(x),0,1])
plt.show()
