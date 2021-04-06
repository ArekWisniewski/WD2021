# Stwórz 3 klasy: Materiał, Ubrania, Swetry. Klasa: Materiał
# Atrybuty:
# •	rodzaj,
# •	długość
# •	szerokość
# Metody:
# •	konstruktor
# •	wyświetl_nazwę
# Klasa: Ubrania
# Atrybuty:
# •	rozmiar
# •	kolor
# •	dla_kogo
# Metody:
# •	wyświetl_dane – do wyświetlania informacji o ubraniu
# klasa: Sweter
# Atrybuty:
# •	rodzaj_swetra – np. Rozpinany, z golfem itd.
# Metody:
# •	wyświetl_dane
# Ubrania dziedziczą po klasie Materiał, a Swetry po klasie Ubrania. Stwórz kilka instancji obiektów i sprawdź, które metody można wykorzystać.

class Material:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.r=rodzaj
        self.dl=dlugosc
        self.szer=szerokosc

    def wyswietl_nazwe(self):
        return (self.r, self.dl, self.szer)

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.ro=rozmiar
        self.k=kolor
        self.dla=dla_kogo
    def wyswietl_dane(self):
        return (self.ro, self.k, self.dla)

class Sweter(Ubrania):
    def __init__(self,rodzaj_swetra):
        self.rodzaj=rodzaj_swetra

    def wyswietl_dane(self):
        return (self.rodzaj)

mat1=Material('bawelna', 40, 40)

print(mat1.wyswietl_nazwe())

ubr1=Ubrania('xxxl','czarny','meska')

print(ubr1.wyswietl_dane())

swe=Sweter('rozpinany')

print(swe.wyswietl_dane())
