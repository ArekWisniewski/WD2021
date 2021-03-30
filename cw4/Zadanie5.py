# Utwórz klasę, która definiuje ciągi arytmetyczne. Wartości powinny być przechowywane jako atrybut. Klasa powinna mieć metody:
# wyświetl_dane – drukuje elementy na ekran
# pobierz_elementy– pobiera konkretne wartości ciągu od użytkownika
# pobierz_parametry – pobiera pierwsza wartość i różnicę od użytkownika oraz ilość elementów ciągu do wygenerowania.
# policz_sume – liczy sume elementow
# policz_elementy – liczy elementy jeśli pierwsza wartość i różnica jest podana
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class ciag_arytmetyczny:
    def __init__(self):
        self.elementy = {}
    def wyswietl_dane(self):
        for i in sorted(self.elementy.keys()):
            print('a('+str(i)+') = '+str(self.elementy[i]))
        if(len(self.elementy) == 0):
            print('ciąg nie posiada żadnych elementów do wyświetlenia')
    def pobierz_elementy(self, numer, wartosc):
        self.elementy[numer] = wartosc
    def pobierz_parametry(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
    def policz_sume(self):
        suma = 0
        for i in self.elementy:
            suma += self.elementy[i]
        return suma
    def policz_elementy(self):
        try:
            for i in range(1, self.n+1, 1):
                self.elementy[i] = self.a1 + (i-1)*self.r
        except AttributeError:
            print('nie podano parametrów')

ciag = ciag_arytmetyczny()
ciag.wyswietl_dane()
ciag.pobierz_elementy(4, 6.6)
ciag.pobierz_elementy(1, 1.6)
ciag.pobierz_elementy(51, 1.6)
ciag.wyswietl_dane()
print()
ciag.pobierz_parametry(1,1,10)
ciag.policz_elementy()
ciag.wyswietl_dane()
print('suma elementów ciągu:',ciag.policz_sume())