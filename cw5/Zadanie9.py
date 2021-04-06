# Przepisz jeden z napisanych przez siebie iteratorów na generator.

def Wspak(dane):
    for i in range(len(dane) - 1, -1, -1):
        yield dane[i]


tablica = Wspak([1, 2, 3])
print('tablica [1, 2, 3]', end=' ')
print('[', end='')
print(next(tablica), end=', ')
print(next(tablica), end=', ')
print(next(tablica), end=']')
print()