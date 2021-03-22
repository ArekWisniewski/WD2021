# Wykorzystując poprzedni przykład zdefiniuj funkcję, która będzie liczyć iloczyn elementów ciągu.

a=float(input('a_1='))
r=float(input('r='))
n=int(input('n='))

def iloczyn(a,r,n):
    ilo=a
    for i in range(1,n):
        ilo=ilo*(a+(i)*r)
    return ilo

print(iloczyn(a,r,n))