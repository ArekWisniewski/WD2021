# Dodaj drugi wykres funkcji sinus do zadania 3 i zmodyfikuj parametry funkcji,
# tak aby osiągnąć efekt podobny do tego na poniższym zrzucie ekranu.

import numpy as np
import matplotlib.pyplot as plt

x= np.arange(0,30,0.1)
s1= 2+np.sin(x)
s2= np.sin(-x)
plt.plot(x,s1,label='sin(x)')
plt.plot(x,s2,label='sin(x)')
plt.xlabel('x')
plt.ylabel('sin(x)')
plt.title('Wykres sin(x), sin(x)')
plt.legend(loc=6)
plt.show()