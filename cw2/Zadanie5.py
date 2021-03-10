#Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:
#czy a zawiera się w przedziale (0,10> oraz czy jednocześnie a>b lub b>c.
# Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.

a = int(input("Podaj a\n"))
b = int(input("Podaj b\n"))
c = int(input("Podaj c\n"))
if a < 10 and a >= 0:
    print("a nie należy do przedziału (0,10>")
if a > b or b > c:
    print("a > b lub b > c spełnione")
else:
    print("a > b lub b > c nie spełnione")