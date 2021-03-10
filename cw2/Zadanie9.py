#Napisz skrypt, który odczytuje od użytkownika liczbę wielocyfrową i sumuje jej cyfry.
# Wynik wyświetla na ekranie. Wykorzystaj pętle while.

l=int(input("Podaj wielocyfrowa liczbę\n"))
suma = 0
while l > 0:
    suma+=l%10
    l //= 10
print(suma)