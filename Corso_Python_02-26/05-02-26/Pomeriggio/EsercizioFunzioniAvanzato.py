#Fibonacci Advanced Function Exercise

#Funzione di controllo numero positivo
def check_p(num):
    if num < 0:
        return False
    return True

#Funzione per generare la sequenza di Fibonacci fino al n-esimo termine
#Cosa fa la successione di fibonacci? Praticamente ogni numero è la somma dei due precedenti, partendo da 0 e 1.
def fibo_il_grande(n):
    a, b = 0, 1
    seq = []
    for _ in range(n):
        seq.append(a)
        a, b = b, a+b
    return seq


while True:
    print("Benvenuto al gioco 'Fibonacci'!\n")
    while True:
        n = int(input("Inserisci un numero positivo: "))
        # Controllo se il numero è positivo tramite la funzione
        if not check_p(n):
            print("Per favore, inserisci un numero positivo.\n")
            continue
        else:
            break
    # Genero la sequenza di Fibonacci fino al n-esimo termine tramite la funzione
    print(f"La sequenza di Fibonacci fino al {n}° termine è:\n{fibo_il_grande(n)}\n")
    
    p = input("Vuoi giocare di nuovo? (s/n): ")
    if p.lower() != 's':
        print("Grazie per aver giocato! Arrivederci.")
        break