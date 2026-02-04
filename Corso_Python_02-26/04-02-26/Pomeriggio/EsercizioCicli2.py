# Controllo numeri primi iterato per 5 volte
on = True
count = 0
while on:
    n = int(input("Inserisci un numero per controllare se è primo: "))
    if n > 0:
        x = n % 2
        if x == 1:
            count += 1
            print(f"Il numero {n} è primo.\nCount: {count}")
        else:
            print(f"Il numero {n} non è primo.")
    else:
        print("Inserisci un numero positivo.")
    if count == 5:
        on = False