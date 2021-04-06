# Za pomocą funkcji isinstance() oraz issubclass() sprawdź wynik dla instancji obiektu Pracownik oraz Menadzer dla klas Osoba, Pracownik i Manadzer.

class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


adrian = Menadzer("Adrian", "Mikulski", 12000)


print(adrian.przedstaw_sie())
print('isinstance')
print('(adrian, Osoba):', isinstance(adrian, Osoba))
print('(adrian, Pracownik):', isinstance(adrian, Pracownik))
print('(adrian, Menadzer):', isinstance(adrian, Menadzer))
print("issubclass:")
print('(Menadzer, Pracownik):', issubclass(Menadzer, Pracownik))
print('(Menadzer, Osoba):', issubclass(Menadzer, Osoba))
print('(Osoba, Pracownik):', issubclass(Osoba, Pracownik))
print('(Osoba, Menadzer):', issubclass(Osoba, Menadzer))
print('(Pracownik, Osoba):', issubclass(Pracownik, Osoba))
print('(Pracownik, Menadzer):', issubclass(Pracownik, Menadzer))