# Esercizio riassuntivo 1 - con Variabili(ok), Condizioni(ok), Cicli(ok) e funzioni(ok)
# Dammi un idea senza scrivermi il codice ovviamente.
"""Crea un programma che simuli un gioco di dadi. Il giocatore lancia due dadi e somma i risultati.
Se la somma è 7 o 11, il giocatore vince. Se la somma è 2, 3 o 12, il giocatore perde.
In caso contrario, il giocatore può scegliere se lanciare di nuovo i dadi o fermarsi. 
Se decide di lanciare di nuovo, deve ottenere la stessa somma per vincere, altrimenti perde."""

import random
from termcolor import colored
import sys

# Funzioni per il gioco dei dadi
def lanciaBroski():
    return random.randint(1, 6), random.randint(1, 6)

# Funzione per sommare i risultati dei dadi
def sommaBroski(a, b):
    return a + b

# Funzione per controllare se il giocatore ha vinto, perso o deve continuare a giocare
def controlloBroski(somma):
    if somma in [7, 11]:
        return f"VittoBroski -> {somma}"
    elif somma in [2, 3, 12]:
        return f"PerditoBroski -> {somma}"
    else:
        return f"ContinuaBroski -> {somma}"

# Inizio ad usare il primo ciclo
while True:
    #inizializzo la lista dei risultati dei dadi
    l = []
    domanda = colored("Ciao Broski benvenuto all'inferno dei dadoski, vuoi giocare? (si/no): ", "white","on_red", ['bold', 'blink'])
    r = input(domanda)
    # Controllo se l'utente vuole giocare con le condizioni
    if r.lower() != "si":
        print(colored("\nOk, magari vai lo stesso all'inferno broski.", "white", "on_red", ['bold', 'blink']))
        exit()
    else:
        print(colored("\nOttimo, sei entrato nell'inferno dei dadi, buona fortuna!", "white", "on_red", ['bold', 'blink']))
        
    while True:
    #""" Lancio i dadi e sommo i risultati, poi li aggiungo ad una lista
    # Uso la funzione lanciaBroski per lanciare i dadi,
    # la funzione sommaBroski per sommare i risultati dei dadi e
    # la funzione controlloBroski per controllare se il giocatore ha vinto, perso o deve continuare a giocare.
        risultato = controlloBroski(sommaBroski(*lanciaBroski()))
        l.append(risultato)
        print(colored(f"\nRisultato: {risultato}", "cyan"))
        
        prompt_game = colored("\nVuoi lanciare di nuovo, uscire o vedere la lista? (exit, lista, ancora): ", "white", "on_red", ['bold', 'blink'])
        rr = input(prompt_game)
        if rr.lower() == "exit":
            print(colored("\nOk, magari vai lo stesso all'inferno broski, ma strisciando.", "red"))
            exit()

        elif rr.lower() == "lista":
            print(colored("\nEcco la lista dei tuoi tentativi:", "red"))
            print(colored(str(l), "yellow"))
            s = input(colored("\nVuoi continuare a giocare? (si/no): ", "white", "on_red", ['bold', 'blink']))
            if s.lower() != "si":
                print(colored("\nOk, magari vai lo stesso all'inferno broski, ma strisciando.", "red"))
                exit()
        else:
            print(colored(f"\nRisultato: {risultato}", "cyan"))
            print(colored("Si continua!", "white", "on_red", ['bold', 'blink']))