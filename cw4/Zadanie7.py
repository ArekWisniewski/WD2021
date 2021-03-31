# Stwórz klasę Robot, która będzie sterować ruchami robota. Klasa powinna przechowywać współrzędne x, y, krok (stała wartość kroku dla robota), i powinna mieć następujące metody:
# konstruktor – który nadaje wartość dla x, y i krok
# idz_w_gore(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_dol(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_lewo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# idz_w_prawo(ile_krokow) – metoda która przesuwa robota o ile_krokow*krok w odpowiednim kierunku i ustawia nowe wartości współrzędnych x i y
# pokaz_gdzie_jestes() – metoda, która wyświetla aktualne współrzędne robota

class robot:
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

robot = robot(0, 0, 1)
robot.pokaz_gdzie_jestes()
robot.idz_w_gore(1000)
robot.pokaz_gdzie_jestes()
robot.idz_w_dol(523)
robot.pokaz_gdzie_jestes()
robot.idz_w_lewo(25)
robot.pokaz_gdzie_jestes()
robot.idz_w_prawo(50)
robot.pokaz_gdzie_jestes()
