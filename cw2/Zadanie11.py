#Napisz skrypt, który rysuje diament. Użytkownik podaje wysokość nie mniej jak 3 i nie więcej jak 9.

wysokosc = int(input('Podaj wysokosc: '))
if 3 <= wysokosc <= 9:
    for x in range(1, wysokosc+1):
        if x % 2:
            print((x * 'O').center(wysokosc, ' '))
    for x in reversed(range(1, wysokosc+1)):
        if x % 2 and x is not wysokosc:
            print((x * 'O').center(wysokosc, ' '))
            
            
# n = 9
#for a1 in range(1, (n+1)//2 + 1): #od rzedu 1 to 5
#    for a2 in range((n+1)//2 - a1):
#        print(" ", end = "")
#    for a3 in range((a1*2)-1):
#        print("*", end = "")
#    print()

#for a1 in range((n+1)//2 + 1, n + 1): # od rzedu 6 to 9
#    for a2 in range(a1 - (n+1)//2):
#        print(" ", end = "")
#    for a3 in range((n+1 - a1)*2 - 1):
#        print("*", end = "")
#    print()
    
