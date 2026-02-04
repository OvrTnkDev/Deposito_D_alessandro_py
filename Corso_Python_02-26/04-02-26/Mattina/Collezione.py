# Creazione di una lista di numeri interi
numeri = [1,2,3,4,5]
# Creazione di una lista di nomi
nomi= ["Alice", "Bob", "Charlie"]
# Creazione di una lista mista
mista = [1, "Due", True, 4.5]
# Accesso agli elementi della lista
print(numeri[0])  # Primo elemento: 1
print(nomi[1])    # Secondo elemento: Bob
print(mista[2])   # Terzo elemento: True

# lista di liste
liste_di_liste = [numeri,nomi,mista]
print(liste_di_liste[1][2])  # Accesso a "Charlie"

# Metodi delle liste
print(len(numeri))  # Lunghezza della lista numeri: 5
numeri.append(6)    # Aggiunge 6 alla fine della lista
print(numeri)       # Ora numeri è [1, 2, 3, 4, 5, 6]
numeri.remove(3)    # Rimuove il valore 3 dalla lista  
print(numeri)       # Ora numeri è [1, 2, 4, 5, 6]
numeri.insert(2, 3) # Inserisce il valore 3 alla posizione 2
print(numeri)       # Ora numeri è [1, 2, 3, 4, 5, 6]
numeri.sort()      # Ordina la lista
print(numeri)      # Ora numeri è [1, 2, 3, 4, 5, 6]
numeri.reverse()   # Inverte l'ordine della lista
print(numeri)      # Ora numeri è [6, 5, 4, 3, 2, 1]

# Creazione d una tupla di numeri interi
tupla_numeri = (1, 2, 3, 4, 5)
# Accesso agli elementi della tupla
print(tupla_numeri[0])  # Primo elemento: 1
tupla_numeri[5] = 6  # Questo genererà un errore perché le tuple sono immutabili

# Unpacking di una tupla
punto = 3, 4 # Crea una tupla (3, 4)
x, y = punto
print(x,y)  # Stampa: 3 4

# Creazione di un set di numeri interi
set1 ={[1,2,3,4,5]}  # Questo genererà un errore perché le liste non sono hashable
set2 = {1,2,3,4,5}   # Creazione corretta di un set
# Aggiunta di un elemento al set
set2.add(6)
print(set2)  # Ora set2 è {1, 2, 3, 4, 5, 6}
# Rimozione di un elemento dal set
set2.remove(3)
print(set2)  # Ora set2 è {1, 2, 4, 5, 6}
# Verifica dell'appartenenza di un elemento al set
print(4 in set2)  # Stampa: True
print(3 in set2)  # Stampa: False

# Operazioni tra set, come union, intersezione, differenza e differenza simmetrica
setA = {1, 2, 3, 4}
setB = {3, 4, 5, 6}

# Unione
set_union = setA.union(setB)
print(set_union)  # Stampa: {1, 2, 3, 4, 5, 6}
# Intersezione
set_intersection = setA.intersection(setB) # Preleva gli elementi comuni tra setA e setB
print(set_intersection)  # Stampa: {3, 4}
# Differenza
set_difference = setA.difference(setB) # Preleva gli elementi che sono in setA ma non in setB
print(set_difference)  # Stampa: {1, 2}
# Differenza simmetrica
set_sym_diff = setA.symmetric_difference(setB) # Preleva gli elementi che sono in setA o in setB ma non in entrambi
print(set_sym_diff)  # Stampa: {1, 2, 5, 6}