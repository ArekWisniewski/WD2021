# Stwórz listę składającą się z wartości zmiennoprzecinkowych a następnie zapisz do innej zmiennej jej kopię przekonwertowaną na typ int64.

import numpy as np
a = np.arange(1,2,0.2)
b = a.astype('int64')
print(a)
print(b)