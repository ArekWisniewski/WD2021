#Napisz skrypt, który rysuje wieżę z literek.
# Użytkownik podaje wysokość wieży ale nie więcej jak 10.

from sys import *
w=int(input("Podaj wysokość wieży\n"))
for i in range(w):
    for j in range(i+1):
        stdout.write("A")
    stdout.write('\n')