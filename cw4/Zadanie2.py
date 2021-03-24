# Odczytaj plik z poprzedniego zadania i wyświetl jego zawartość w konsoli.

plik = open("Zadanie1.txt","r")
wiersze = plik.readlines()
plik.close()
print(wiersze)