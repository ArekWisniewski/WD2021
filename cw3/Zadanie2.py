# Wygeneruj losowo macierz 4x4 i wykorzystując Python Comprehension zdefiniuj listę,
# która będzie zawierała tylko elementy znajdujące się na przekątnej

import random

macierz = [[random.randint(0, 9) for i in range (0, 4, 1)] for j in range (0, 4, 1)]
przekatna = [macierz[i][j] for j in range (0, 4, 1) for i in range (0, 4, 1) if i == j]
print(macierz)
print('Przekątna: ',przekatna)