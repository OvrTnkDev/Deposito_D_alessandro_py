"""Scrivete un programma che utilizza il cifrario di Cesare per criptare una
parola o decriptarla.
Il Cifrario di Cesare è un algoritmo di crittografia che consiste nello spostare
ciascuna lettera di una certa quantità di posti nell'alfabeto. Per utilizzarlo, si
sceglie una chiave (scelta dall’utente) che rappresenta il numero di posti
di cui ogni lettera dell'alfabeto verrà spostata: ad esempio, se si sceglie
una chiave di 3, la lettera A diventerà D, la lettera B diventerà E e così via.
Per decifrare un messaggio cifrato con il cifrario di Cesare bisogna
conoscere la chiave utilizzata e spostare ogni lettera indietro di un numero
di posti corrispondente alla chiave."""


def cripta(testo, chiave):
    risultato = ""

    for carattere in testo.lower():
        if carattere.isalpha():  # Controllo se è lettera
            # Calcolo il nuovo carattere spostato
            # ord('a') è usato per mantenere il ciclo all'interno dell'alfabeto
            # il modulo 26 assicura che si torni all'inizio dell'alfabeto dopo 'z'
            # ord(carattere) - ord('a') calcola la posizione della lettera nell'alfabeto (0-25)
            nuovo = (ord(carattere) - ord('a') + chiave) % 26 + ord('a')
            risultato += chr(nuovo)
        else:
            risultato += carattere # rimane invariato

    return risultato

def decriptaStringa(stringa_criptata, spostamento):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    stringa_decriptata = ''
    for c in stringa_criptata:
        stringa_decriptata = stringa_decriptata + alfabeto[(alfabeto.index(c) - spostamento) % 26]
    return stringa_decriptata


while True:
    scelta = input("Vuoi criptare o decriptare(0 per uscire)? (c/d): ")
    if scelta == '0':
        print("Uscita dal programma.")
        break
    if scelta == 'c':
        testo = input("Inserisci il testo da criptare: ")
        chiave = int(input("Inserisci la chiave (numero di posti): "))
        print("Testo criptato:", cripta(testo, chiave))
    elif scelta == 'd':
        testo_criptato = input("Inserisci il testo da decriptare: ")
        chiave = int(input("Inserisci la chiave (numero di posti): "))
        print("Testo decriptato:", decriptaStringa(testo_criptato, chiave))
    else:
        print("Scelta non valida. Riprova.")