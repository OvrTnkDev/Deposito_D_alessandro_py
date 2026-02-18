"""Create un programma in 2 parti:
- prima parte genera 5 numeri
casuali e li salva su un file
- seconda parte, rilegge il file e l’utente dovrà cercare di indovinarne almeno 2 di quei numeri
oppure avrà perso."""

import random as r

FILE_NAME = r"Corso_Python_02-26/18-02-26/Mattina/db/numbers.txt"

# generazione dei numeri
def generate_numbers():
    return [r.randint(1, 100) for _ in range(5)]

# funzioni per scrivere
def write_file(numbers):
    with open(FILE_NAME, "w") as f:
        f.write(numbers)

# funzione per leggere
def read_file():
    with open(FILE_NAME,"r") as file:
        contenuto = file.read()
    return contenuto


# funzione principale del programma che gestisce la logica del gioco
def main():
    numbers =",".join([str(n) for n in generate_numbers()])
    write_file(numbers)


    # utilizzo una list comprehension per leggere e convertire i numeri in interi
    cont = read_file()
    listaR = cont.split(",")
    matrice = [int(num) for num in listaR]
    
    
    print("Indovina almeno 2 dei numeri generati!")
    # l'utente ha 5 tentativi per indovinare i numeri
    x = 0
    while x < 5:
        guess = input(f"tentativo {x+1} - Inserisci un numero: ")
        try:
            guess = int(guess)  # converto l'input in un intero
        except ValueError as e:
            print(f"Per favore, inserisci un numero valido.", e)
            continue  # salta al prossimo tentativo se l'input non è un numero
        if guess in matrice:
            print("Hai indovinato un numero!")
            matrice.remove(guess)  # rimuove il numero indovinato per evitare duplicati
        else: print("Numero sbagliato!")
        x += 1  # incrementa il contatore dopo ogni tentativo

    if len(matrice) <= 3:  # se sono stati indovinati almeno 2 numeri
        print("Hai vinto!")
    else: print("Hai perso! I numeri erano:", matrice)


# esecuzione del programma
main()