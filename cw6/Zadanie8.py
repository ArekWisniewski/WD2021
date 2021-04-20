# Napisz funkcję, która:
# - jako parametr wejściowy będzie przyjmowała tablicę wielowymiarową numpy oraz parametr ‘kierunek’,
# - parametr kierunek określa czy tablica wejściowa będzie dzielona w pionie czy poziomie
# - funkcja dzieli tablicę wejściową na pół (napisz warunek, który wyświetli komunikat,
# że ilość wierszy lub kolumn, w zależności od kierunku podziału, nie pozwala na operację)

import numpy as np

def funkcja(macierz, kierunek):
    if kierunek == 'góra' or kierunek == 'dół':
        if len(macierz) % 2 == 0:
            if kierunek == 'góra':
                return macierz[0:(len(macierz)//2)]
            if kierunek == 'dół':
                return macierz[(len(macierz)//2):]
        else:
            print('liczba wierszy nie pozwala no podział')
    if kierunek == 'lewo' or kierunek == 'prawo':
        if len(macierz[0]) % 2 == 0:
            if kierunek == 'lewo':
                return macierz[:, 0:(len(macierz[0])//2)]
            if kierunek == 'prawo':
                return macierz[:, (len(macierz[0])//2):]
        else:
            print('liczba kolumn nie pozwala no podział')

macierz = np.ones((4, 4), dtype='int')
liczba = 0
for i in range(0, 4, 1):
    for j in range(0, 4, 1):
        macierz[i][j] = liczba
        liczba += 1

print('macierz:')
print(macierz)
print('góra:')
print(funkcja(macierz, 'góra'))
print('dół:')
print(funkcja(macierz, 'dół'))
print('lewo:')
print(funkcja(macierz, 'lewo'))
print('prawo:')
print(funkcja(macierz, 'prawo'))