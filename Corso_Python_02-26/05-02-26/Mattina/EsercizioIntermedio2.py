while True:
    num = input("Inserisci 2 numeri separati da uno spazio (es. 6 12): ")
    # converti la stringa di input in una lista di numeri interi con map e list
    # map serve per applicare la funzione int a ogni elemento della lista ottenuta da num.split()
    num_list = list(map(int, num.split()))
    
    # controlla che l'utente abbia inserito esattamente 2 numeri
    if len(num_list) != 2:
        print("Per favore, inserisci esattamente 2 numeri.\n")
        continue
    
    # Ordino la lista per assicurarmi che x sia minore di y, altrimenti il range non parte
    num_list.sort()
    x, y = num_list
    
    for i in range(x, y+1):
        # stampare solo se è un numero primo
        if i > 1:  # i numeri primi sono maggiori di 1
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                print(i)
    continua = input("Vuoi continuare? (s/n): ").lower()
    if continua != 's':
        print("Uscita dal programma.")
        break