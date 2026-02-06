# Decoratore
from curses import wrapper


def decor(func):
    def wrapper():
        print("Inizio della funzione decorata")
        func()
        print("Fine della funzione decorata")
    return wrapper

# Esempio di decoratore
@decor
def saluta():
    print("Ciao, come stai? Sono il decoratore!")

# Decoratore con argomenti per la funzione decorata
def decoratore_con_argomenti(funzione):
    def wrapper(*args, **kwargs):
        print("Prima")
        risultato = funzione(*args, **kwargs)
        print("Dopo")
        return risultato
    return wrapper

@decoratore_con_argomenti
def somma(a, b):
    print(a+b)
    return a + b

# Decoratore per loggare le chiamate a una funzione
def logger(funzione):
    def wrapper(*args, **kwargs):
        print(f"Chiamata a {funzione.__name__} con argomenti: {args} e {kwargs}")
        risultato = funzione(*args, **kwargs)
        print(f"Risultato di {funzione.__name__}: {risultato}")
        return risultato
    return wrapper

@logger
def moltiplica(a, b):
    return a * b

# Esempio di decoratore
saluta()

# Esempio di decoratore con argomenti
print("risultato è ", somma(3, 4))

# Chiamata alla funzione decorata
print(moltiplica(3, 4))