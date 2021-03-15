# Zdefiniuj funkcję, która będzie badać monotoniczność funkcji liniowej:
# y = a x + b
# Funkcja jest rosnąca gdy a>0, malejąca jeżeli a<0, stała gdy a=0 i w zależności od tego będzie wyświetlać odpowiedni komunikat

a=float(input('podaj a '))

def czy_ros(a):
    if a>0:
        print('funkcja rosnąca')
    if a<0:
        print('funkcja malejąca')
    if a==0:
        print('funkcja stała')

czy_ros(a)