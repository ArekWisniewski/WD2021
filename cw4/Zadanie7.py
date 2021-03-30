# Stwórz klasę Robaczek, która będzie sterować ruchami Robaczka. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla Robaczka), i powinna mieć następujące metody:
# •	konstruktor – który nadaje wartość dla x, y i krok
# •	idz_w_gore(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	idz_w_dol(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	idz_w_lewo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	idz_w_prawo(ile_krokow) – metoda która przesuwa robaczka o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# •	pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne Robaczka
# Stwórz instancję klasy i sprawdź jak działają wszystkie metody

class robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile_krokow):
        self.y += ile_krokow*self.krok
    def idz_w_dol(self, ile_krokow):
        self.y -= ile_krokow*self.krok
    def idz_w_lewo(self, ile_krokow):
        self.x -= ile_krokow*self.krok
    def idz_w_prawo(self, ile_krokow):
        self.x += ile_krokow*self.krok
    def pokaz_gdzie_jestes(self):
        print('Aktualna pozycja: ('+str(self.x)+', '+str(self.y)+')')

robak = robaczek(0, 0, 1)
robak.pokaz_gdzie_jestes()
robak.idz_w_gore(1000)
robak.pokaz_gdzie_jestes()
robak.idz_w_dol(523)
robak.pokaz_gdzie_jestes()
robak.idz_w_lewo(25)
robak.pokaz_gdzie_jestes()
robak.idz_w_prawo(50)
robak.pokaz_gdzie_jestes()