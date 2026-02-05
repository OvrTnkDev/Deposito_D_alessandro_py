#Indovina il numero
import random as r

#Funzione di controllo numero positivo
def check_p(num):
    if num < 0:
        return False
    return True

#Funzione per generare un numero casuale tra 0 e n
def n_rnd(n):
    return r.randint(0, n)

while True:
    print("Benvenuto al gioco 'Indovina il numero'!\n")
    while True:
        n = int(input("Inserisci un numero positivo: "))
        # Controllo se il numero è positivo tramite la funzione
        if not check_p(n):
            print("Per favore, inserisci un numero positivo.\n")
            continue
        else:
            break
        
    # Genero un numero casuale tra 0 e n tramite la funzione
    n_random = n_rnd(n)
    tentativi = 0
    print(f"Ho scelto un numero casuale tra 0 e {n}. Prova a indovinarlo!\n")
    
    while True:
        t = int(input("Inserisci il tuo tentativo: "))
        if not check_p(t):
            print("Per favore, inserisci un numero positivo.\n")
            continue
        else:
            tentativi += 1
            if t < n_random:
                print("Troppo basso! Riprova.\n")
            elif t > n_random:
                print("Troppo alto! Riprova.\n")
            else:
                print(f"Congratulazioni! Hai indovinato il numero {n_random} in {tentativi} tentativi.\n")
                break
    p = input("Vuoi giocare di nuovo? (s/n): ")
    if p.lower() != 's':
        print("Grazie per aver giocato! Arrivederci.")
        break