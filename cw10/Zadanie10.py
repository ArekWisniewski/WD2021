# Poszukaj w bibliotece wykresów (https://matplotlib.org/gallery/index.html) przykładów z adnotacjami
# (annotating plots) na wykresach i dodaj adnotacje
# do dwóch wybranych stworzonych wcześniej wykresów.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.subplot(1,2,1)
x = np.arange(0, 30.1, 0.1)
s = np.sin(x)
c = np.cos(x)
plt.plot(x, s, label='sin(x)')
plt.plot(x, c, label='cos(x)')
plt.annotate('sin(x)=0',
            xy=(0, 0), xycoords='data',
            xytext=(0, -1), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='center', verticalalignment='top')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')

plt.subplot(1,2,2)
x = np.arange(1, 21)
plt.plot(x, 1 / x, label='f(x)=1/x')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.axis([0, len(x), 0, 1])
plt.annotate('f(5)=0.2',
            xy=(5, 0.2), xycoords='data',
            xytext=(7.5, 0.6), textcoords='data',
            arrowprops=dict(facecolor='red', shrink=0.05),
            horizontalalignment='left', verticalalignment='bottom')
plt.show()