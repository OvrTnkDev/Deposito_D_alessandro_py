# Funzioni in Python con 1 parametro senza return
def salta(nome):
    print(f"{nome} ha fatto HOOOP!")

# Funzioni in Python con 2 parametri senza return
def salta_n_volte(nome, salto):
    for _ in range(salto):
        print(f"{nome} ha fatto HOOOP {_+1} volte!")

# Funzione per lista splat senza return
def listaX (lista : list):
    for e in lista:
        print(f"{lista.index(e)+1}° Elemento: {e}")
        
# Funzione con return
def somma(a,b):
    return a + b

# Esempi di utilizzo delle funzioni
salta("Luigino")
salta_n_volte("Pippo", 5)
listaX([*range(0,31,3)])
print(f"La somma è : {somma(5,10)}")