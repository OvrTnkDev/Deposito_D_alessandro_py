#Esercizio 1
x = int(input("Inserisci un numero: "))
#Condizione semplice
if (x != 0):
    print("Il numero è diverso da zero")
    y = int(input("Inserisci un altro numero: "))
    #Condizione con elif
    if (y < x):
        print("Il secondo numero è minore del primo")
    elif (y == x):
        print("Il secondo numero è uguale al primo")
        z = int(input("Inserisci un altro numero ancora: "))
        if (z > y):
            print("Il terzo numero è maggiore del secondo")
        else:
            print("Il terzo numero è minore o uguale al secondo")
    else:
        print("Il secondo numero è maggiore del primo")
#Condizione con else
else:
    print("Il numero è zero quindi CIAO")