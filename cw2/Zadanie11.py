#Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9.

wysokosc = int(input('Podaj wysokosc: '))
if 3 <= wysokosc <= 9:
    for x in range(1, wysokosc+1):
        if x % 2:
            print((x * 'O').center(wysokosc, ' '))
    for x in reversed(range(1, wysokosc+1)):
        if x % 2 and x is not wysokosc:
            print((x * 'O').center(wysokosc, ' '))