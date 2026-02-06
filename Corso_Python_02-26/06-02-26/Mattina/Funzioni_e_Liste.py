# 18.Esercizio 2:  Funzioni e Liste
# Funzione con cotrollo delle vocali in una parola

def c_vocali (p:str):
    p = p.lower()
    v="aeiou"
    c=0
    for i in p:
        if i in v:
            c+=1
    return c

while True:
    p = input("Inserisci una parola: ")
    print(f"La parola {p} contiene {c_vocali(p)} vocali.\n")
    
    r = input("Vuoi inserire un'altra parola? (s/n): ")
    if r.lower() != 's':
        print("Uscita dal programma.")
        break