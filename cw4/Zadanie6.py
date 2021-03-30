# Utwórz klasę Slowa, która będzie zarządzać różnymi grami słownymi. Klasa powinna przechowywać przynajmniej dwa słowa i metody:
# •	sprawdz_czy_palindrom – metoda sprawdza czy dany wyraz jest palindromem (czytany od początku czy wspak jest taki sam np. kajak)
# •	sprawdz_czy_metagramy – metoda sprawdza czy wyrazy różnią się jedną litera a poza tym są takie same np. mata, tata
# •	sprawdz_czy_anagramy – metoda sprawdza czy wyrazy maja ten sam zestaw liter. Np. mata i tama
# •	wyświetl_wyrazy – wyświetla podane wyrazy
# Stwórz instancję klasy i sprawdź działanie wszystkich metod.

class slowa:
    def __init__(self, slownik):
        self.slownik = slownik
    def sprawdz_czy_palindrom(self, wyraz):
        for i in range(0, len(wyraz)//2, 1):
            if(wyraz[i] != wyraz[-i-1]):
                return False
        return True
    def sprawdz_czy_metagramy(self, wyraz1, wyraz2):
        ile_roznych = 0
        if(len(wyraz1) != len(wyraz2)):
            return False
        for i in range(0, len(wyraz1), 1):
            if(wyraz1[i] != wyraz2[i]):
                ile_roznych += 1
        if(ile_roznych == 1):
            return True
        else:
            return False
    def sprawdz_czy_anagramy(self, wyraz1, wyraz2):
        litery_1 = {}
        litery_2 = {}
        if(len(wyraz1) != len(wyraz2)):
            return False
        for i in range(0, len(wyraz1), 1):
            try:
                litery_1[wyraz1[i]] += 1
            except:
                litery_1[wyraz1[i]] = 1
            try:
                litery_2[wyraz2[i]] += 1
            except:
                litery_2[wyraz2[i]] = 1
        if(len(litery_1) != len(litery_2)):
            return False
        for i in sorted(litery_1):
            try:
                if(litery_1[i] != litery_2[i]):
                    return False
            except:
                return False
        return True
    def wyswietl_wyrazy(self):
        for i in range(0, len(self.slownik), 1):
            print(self.slownik[i])

jakies_slowa = ['adam', 'który', 'tata', 'mata', 'kajak']
obiekt = slowa(jakies_slowa)
print('słowa w obiekcie: ')
obiekt.wyswietl_wyrazy()
print()
for i in obiekt.slownik:
    print('słowo "'+str(i)+'" ', end='')
    if(obiekt.sprawdz_czy_palindrom(i) == True):
        print('jest palindromem')
    else:
        print('NIE jest palindromem')
print()
for i in obiekt.slownik:
    for j in obiekt.slownik:
        print('słowa: "'+str(i)+'" oraz "'+str(j)+'" ', end='')
        if(obiekt.sprawdz_czy_metagramy(i, j) == True):
            print('są metagramami')
        else:
            print('NIE są metagramami')
print()
for i in obiekt.slownik:
    for j in obiekt.slownik:
        print('słowa: "'+str(i)+'" oraz "'+str(j)+'" ', end='')
        if(obiekt.sprawdz_czy_anagramy(i, j) == True):
            print('są anagramami')
        else:
            print('NIE są anagramami')