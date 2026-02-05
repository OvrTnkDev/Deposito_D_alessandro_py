import random

while True:
    while True:
        n = input("Inserisci un numero positivo o 0 per uscire: ")
        if n == '0':
            print("Uscita dal programma.")
            exit()
        # provo a fare il parsing in intero e vedere se  è un numero positivo
        try:
            n = int(n)
            if n > 0:
                break
            else:
                print("Per favore, inserisci un numero positivo.\n")
        # eccezione semmai n non fosse un numero
        except ValueError:
            print(f"{ValueError} Input non valido. Per favore, inserisci un numero positivo.\n")

    # genero una tupla di interi casuali tra 1 e n usanto il modulo random
    tupla_casuale = tuple(random.randint(1,n) for _ in range(n))
    print(f"Tupla di numeri casuali generata tra 1 e {n}: {tupla_casuale}\n")
    
    # Calcolo della somma degli elementi della tupla
    somma_tupla = sum(tupla_casuale)
    print(f"La somma degli elementi della tupla è: {somma_tupla}\n")
    
    # Calcolo la somma con un ciclo for
    somma_tupla2 = 0
    for numero in tupla_casuale:
        somma_tupla2 += numero
    print(f"La somma calcolata con il ciclo for è: {somma_tupla2}\n")
    
    # Stampo tutti i numeri dispari nella lista tramite una list comprehension
    # list comprehension è un modo compatto per creare liste in Python e serve per filtrare o trasformare gli elementi di una lista esistente
    numeri_dispari = [num for num in tupla_casuale if num % 2 != 0]
    print(f"I numeri dispari nella lista sono: {numeri_dispari}\n")
    
    # Verifico se ci sono numeri primi nella lista usando una funzione lambda
    # all verifica se tutti gli elementi in un iterabile soddisfano una condizione o meglio se tutti i resti della divisione sono diversi da zero
    is_prime = lambda x: all(x % i != 0 for i in range(2, int(x**0.5) + 1)) and x > 1
    
    # Creo una lista dei numeri primi trovati nella lista casuale
    numeri_primi = [num for num in tupla_casuale if is_prime(num)]
    
    # Stampo i numeri primi trovati se ce ne sono
    if numeri_primi:
        print(f"I numeri primi nella lista sono: {numeri_primi}\n")
    else:
        print("Nessun numero primo trovato nella lista.\n")
    
    # Sommo la lista e controllo se il prodotto è pari o dispari
    if is_prime(somma_tupla):
        print(f"La somma {somma_tupla} è un numero primo.\n")
    else:
        print(f"La somma {somma_tupla} non è un numero primo.\n")
        
    # Chiedo si eliminare un numero dalla tupla, se si la trasormo prima in lista
    elimina = input("Vuoi eliminare un numero dalla tupla? (s/n): ")
    if elimina.lower() == 's':
        print(f"Quale vuoi eliminare?\n Tupla attuale: {tupla_casuale}")
        num_del = int(input("Inserisci il numero da eliminare: "))
        
        # Trasformo la tupla in lista per poter eliminare l'elemento
        lista_tmp = list(tupla_casuale)
        if num_del in lista_tmp:
            lista_tmp.remove(num_del)
            tupla_casuale = tuple(lista_tmp)
            print(f"Tupla aggiornata: {tupla_casuale}\n")
        else:
            print(f"Il numero {num_del} non è presente nella tupla.\n")