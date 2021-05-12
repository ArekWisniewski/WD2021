# Z repozytorium UCI (http://archive.ics.uci.edu/ml/index.php) pobierz dataset Iris i za pomocą wykresu punktowego (scattered)
# wyświetl wartość 2 wybranych cech tego datasetu. Dla każdego rodzaju kwiatu użyj innego koloru na wykresie. Przykład można
# znaleźć w galerii wykresów biblioteki matplotlib - link w materiałach matplotlib.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


irys = pd.read_csv('iris.data', sep=',', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
lista = []
for x in irys['class']:
    if x == 'Iris-setosa':
        lista.append('red')
    elif x == 'Iris-versicolor':
        lista.append('blue')
    else:
        lista.append('black')
data = {'x': irys['sepal length'],
        'y': irys['sepal width'],
        'c': lista}
plt.scatter('x', 'y', c='c', data=data)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()