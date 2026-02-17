"""Scrivete un gioco in cui il giocatore 1 inserisce un
numero da 1 a 100 e il giocatore2 ha 5 tentativi per
indovinare il numero.
Il programma fornisce suggerimenti (troppo alto,
troppo basso), termina quando l'utente indovina
correttamente, quando i tentativi finiscono o se
scrive «mi arrendo»."""
# faccio funzione giocatore 2

def player2(number_p1):
    number_2 = int(input("Giocatore 2, inserisci un numero da 1 a 100: "))
    if number_2 == number_p1:
        print("Hai indovinato!")
        return True
    elif number_2 > number_p1:
        print("Troppo alto!")
        return False
    else:
        print("Troppo basso!")
        return False