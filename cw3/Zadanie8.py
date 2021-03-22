# Zdefiniuj funkcję, która zwraca sumę dowolnego ciągu arytmetycznego.
# Funkcja niech przyjmuje jako parametry: a1 (wartość początkowa),
# r (wielkość o ile rosną kolejne elementy) i ile_elementów (ile elementów ma sumować).
# Ponadto funkcja niech przyjmuje wartości domyślne: a1= 1, r=1, ile=10.

a=float(input('a_1='))
r=float(input('r='))
n=float(input('n='))

def suma(a,r,n):
    return ((2*a+((n-1)*r))*n)/2

print(suma(a,r,n))