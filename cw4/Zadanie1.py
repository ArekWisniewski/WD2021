# Wygeneruj liczby podzielne przez 4 i zapisz je do pliku

plik = open("Zadanie1.txt","w")

for x in range (1,10):
    l=x*4
    t=str(l)+" "
    plik.writelines(str(t))
plik.close()
