lista=[]
while True:
    while True:
        scelta = input("0-Esci\n1-Numeri pari\n2-Numeri dispari\n3-Numero primo\n4-Vuoi vedere la lista?\n" +
                       "Seleziona un'opzione (0, 1, 2, 3, 4): ")
        # Gestione dell'uscita
        if scelta == '0':
            print("Uscita dal programma.")
            exit()
            
        # Gestione della visualizzazione della lista
        if scelta == '4':
            break
        
        # Richiesta del numero positivo solo per le opzioni 1, 2 e 3
        if scelta in ['1', '2', '3']:
            n = int(input("Inserisci un numero positivo: "))
            if n > 0:
                break
            else:
                print("Per favore, inserisci un numero positivo.\n")
                continue
    match scelta:
        case '1':
            # Stampare numeri pari fino a n
            list_pari= []
            print(f"Numeri pari da 0 a {n}:")
            for i in range(0, n+1, 2):
                list_pari.append(i)
                print(i)
            lista.append([f"Numero pari {list_pari}"])
        case '2':
            # Stampare numeri dispari fino a n
            list_dispari = []
            print(f"Numeri dispari da 0 a {n}:")
            for i in range(1, n+1, 2):
                list_dispari.append(i)
                print(i)
            lista.append([f"Numero dispari {list_dispari}"])
        case '3':
            #Stampare se è un numero primo tramite if
            is_prime = True
            if n > 1:
                for i in range(2, n):
                    if (n % i) == 0:
                        is_prime = False
                        break
            else:
                is_prime = False # 1 non è primo
            
            if is_prime:
                print(f"{n} è un numero primo.")
                lista.append([f"Numero primo: {n} (SI)"])
            else:
                print(f"{n} non è un numero primo.")
                lista.append([f"Numero primo: {n} (NO)"])
        case '4':
            # Mostrare la lista delle operazioni effettuate
            print("Lista delle operazioni effettuate:")
            if not lista:
                print("La lista è vuota.")
            else:
                for elemento in lista:
                    print(elemento)
        case _:
            print("Opzione non valida. Riprova.\n")
            continue
    
    # Chiedere se l'utente vuole continuare
    e = input("Vuoi continuare? (s/n): ").lower()
    if e != 's':
        print("Uscita dal programma.")
        break