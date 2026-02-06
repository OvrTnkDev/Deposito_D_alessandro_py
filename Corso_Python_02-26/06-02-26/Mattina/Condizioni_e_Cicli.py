# 17.Esercizio 1:  Condizioni e cicli
# 1. Scrivere un programma che chieda all'utente di inserire un numero positivo e stampi tutti i numeri pari da 0 a quel numero.

while True:
    while True:
        # Richiesta del numero positivo solo per le opzioni 1, 2 e 3
        n = int(input("Inserisci un numero positivo: "))
        # Controllo se il numero è positivo tramite if
        if n > 0:
            # Se il numero è positivo, eseguo il ciclo for per stampare i numeri pari da 0 a n
            break
        else:
            print("Per favore, inserisci un numero positivo.\n")
            continue
        
    # Ciclo for per stampare i numeri pari da 0 a n    
    for i in range(1, n+1):
        # Controllo se il numero è pari o dispari tramite if
        if i % 2 == 0:
            print(f"Il numero è pari: {i}")
        else:
            print(f"Il numero è dispari: {i}")
            
    r = input("Vuoi inserire un altro numero? (s/n): ")
    if r.lower() != 's':
        print("Uscita dal programma.")
        break