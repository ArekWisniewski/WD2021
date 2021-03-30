# zadanie 8
# Do klasy z wybranego poprzedniego zadania dołącz funkcję niszczenia obiektu.
class robaczek:
    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def __del__(self):
        print('Obiekt spadł z rowerka XD')
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