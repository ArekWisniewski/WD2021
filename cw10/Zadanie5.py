# Korzystając ze zbioru danych Iris (https://archive.ics.uci.edu/ml/datasets/iris)
# wygeneruj wykres punktowy, gdzie wektor x to wartość ‘sepal length’ a y to ‘sepal width’,
# dodaj paletę kolorów c na przykładzie listingu 6 a parametr s niech będzie wartością absolutną z
# różnicy wartości poszczególnych elementów wektorów x oraz y.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

irys = pd.read_csv('iris.data', sep=',', names=['sepal length', 'sepal width', 'petal length', 'petal width', 'class'])
data = {'x': irys['sepal length'],
        'y': irys['sepal width'],
        'c': np.random.randint(0, 50, 150)}
data['s'] = np.abs(data['x'] - data['y'])
plt.scatter('x', 'y', c='c', s='s', data=data)
plt.xlabel('sepal length')
plt.ylabel('sepal width')
plt.show()