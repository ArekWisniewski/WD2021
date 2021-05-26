# Zmodyfikuj wykres z zadania 1 tak, żeby styl wykresu wyglądał tak jak na poniższym zrzucie ekranu.

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(1,21)
plt.plot(x, 1/x, 'g:>', label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("Wykres funkcji f(x) dla x[1,20]")
plt.axis([0,len(x),0,1])
plt.show()