#Napisz własny iterator, który będzie zwracał tylko samogłoski z przekazanego ciągu tekstowego.
# Zaimplementuj sprawdzanie czy przekazany został string jako argument konstruktora tego iteratora (sprawdź funkcję isinstance()).

class Samogloski:
    def __init__(self, x):
        self.x = x
        self.ix = -1
        self.wynik = isinstance(self.x, str)
        self.napis = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.wynik:
            self.ix = self.ix + 1

            if self.x[self.ix] == "a" or self.x[self.ix] == "e" or self.x[self.ix] == "i" \
                    or self.x[self.ix] == "o" or self.x[self.ix] == "u" or self.x[self.ix] == "y":
                self.napis.append(self.x[self.ix])

        else:
            print("Nie podales typu string")
            raise StopIteration
        return self.napis


wyraz = Samogloski("abeugy")
print(next(wyraz))
print(next(wyraz))
print(next(wyraz))
print(next(wyraz))
print(next(wyraz))
print(next(wyraz))