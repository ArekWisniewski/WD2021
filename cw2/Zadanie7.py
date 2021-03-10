# Napisz pętle, która pobiera liczby od użytkownika i wyświetla ich kwadraty na ekranie.

l = input("Podaj liczbę\n")
for i in range(1, 5, 1):
    print(int(l) * int(l))
    l = input("Podaj liczbę\n")