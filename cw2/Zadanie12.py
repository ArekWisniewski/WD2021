#Napisz skrypt, który wyświetla i oblicza tabliczkę mnożenia od 1 do 100.

from sys import *
for i in range(1,11,1):
    for j in range(1,11,1):
        s=i*j
        stdout.write("%d"%s)
        if(s<10):
            stdout.write(" ")
        stdout.write(" ")
    stdout.write('\n')