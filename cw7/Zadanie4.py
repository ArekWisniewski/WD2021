# Utwórz dwie macierze 1x3 gdzie pierwsza z nich będzie zawierała liczby całkowite, a druga liczby rzeczywiste.
# Następnie wykonaj na nich operację mnożenia.

import numpy as np
a = np.arange(3)
b = np.linspace(np.pi,np.pi,3)
print(a*b)