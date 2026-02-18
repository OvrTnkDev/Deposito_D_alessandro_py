"""Scrivete un programma che utilizza una funzione che accetta
come parametro una stringa passata dall’utente e restituisce in
risposta se è palindroma o no.
Esempio:
‘I topi non avevano nipoti’ è palindroma
‘Ciao’ non è palindroma"""

def palindrom(w1):
    # Rimuove spazi e converte in minuscolo
    w1 = ''.join(c.lower() for c in w1 if c.isalpha())
    # Controlla se la stringa è uguale alla sua inversa
    if w1 == w1[::-1]:
        print(f"La frase '{w1}' è palindroma")
    else:
        print(f"La frase '{w1}' non è palindroma")

while True:
    r = input("Controllo palindromo (0.esci-1.controlla): ")
    
    match r:
        case "0":
            print("Arrivederci")
            break
        
        case "1":
            w1 = input("Inserisci la frase: ")
            palindrom(w1)

        case _:
            print("Riprova, questa scelta non esiste")
            continue