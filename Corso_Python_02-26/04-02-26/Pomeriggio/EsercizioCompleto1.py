on = True
while on:
    n = int(input("Inserisci un numero per controllare se è pari: "))
    if n > 1:
        if n % 2 == 0:
            print(f"Il numero {n} è pari.")
        else:
            print(f"Il numero {n} non è pari.")
    else:
        print("Inserisci un numero maggiore di 1.")