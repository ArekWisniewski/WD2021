# Napisz własny iterator, który będzie zwracał tylko elementy z parzystych indeksów przekazanej kolekcji.
class parzyste:

    def __init__(self, liczby):
        self.liczby=liczby
        self.ind= -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.ind>=len(self.liczby):
            raise StopIteration
        self.ind=self.ind+2
        return self.liczby[self.ind]


tabelka=parzyste([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

print(next(tabelka), end=' ')
print(next(tabelka), end=' ')
print(next(tabelka), end=' ')
print(next(tabelka), end=' ')
print(next(tabelka), end=' ')

