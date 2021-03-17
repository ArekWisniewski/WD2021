# Napisz funkcję, która będzie sprawdzać czy dwie proste są równoległe czy prostopadłe:
# Proste dane równaniami:
# y=a1x+b1, y=a2x+b2, są równolegle gdy a1=a2 prostopadłe gdy a1a2=-1.


a_1=float(input('podaj a_1 '))
a_2=float(input('podaj a_2 '))

def położenie(a_1,a_2):
    if a_1==a_2:
        print('funkcje równoległe')
    elif a_1*a_2==-1:
        print('funkcje prostopadłe')
    else :
        print('funkcje nie są ani równloległe ani prostopadłe')

położenie(a_1,a_2)
