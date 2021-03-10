#Napisz skrypt, który odczytuje liczby od użytkownika i umieszcza je na liście.
# Wykorzystaj pętle while.

lista=[]
while True:
    l=input("Podaj liczbę do umieszczenia na liście\n")
    lista.append(int(l))
    print(lista)