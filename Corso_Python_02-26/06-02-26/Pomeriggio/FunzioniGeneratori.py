
# Funzioni Generator
# Serve per creare un iteratore che restituisce una sequenza di valori, invece di restituire un singolo valore come una funzione normale.
# La parola chiave "yield" viene utilizzata per restituire un valore e sospendere l'esecuzione della funzione, in modo che possa essere ripresa in un secondo momento.

import random as r

def rando_n(n:int):
    yield r.randint(1, n)
    
    
def fibonacci(n: int):
    a,b = 0,1
    while a < n:
        yield a
        a,b = b, a+b

# Esempio di catena di generatori
def catena_generatori():
    yield from range(12)
    yield from rando_n(5)


# Esempi di utilizzo
print(list(fibonacci(next(rando_n(10)))))

# Esempio di catena di generatori
print(list(catena_generatori()))