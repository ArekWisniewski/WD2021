# Wykorzystując komendę with zapisz kilka linijek tekstu do pliku a następnie wyświetl je na ekranie.

with open("Zadanie3.txt", "w") as plik:
    for x in range (0,10):
        l=x*x
        t=str(x)+"^2="+str(l)
        plik.writelines(str(t))
        plik.writelines("\n")

with open("Zadanie3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")