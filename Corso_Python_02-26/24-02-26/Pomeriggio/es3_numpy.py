"""
Esercizio 3: Operazioni con Fancy Indexing
Creare un array NumPy di forma (4, 4) contenente numeri casuali interi tra 10 e 50.
Utilizzare fancy indexing per selezionare e stampare gli elementi agli indici (0, 1), (1, 3), (2, 2) e (3, 0).
Utilizzare fancy indexing per selezionare e stampare tutte le righe dispari dell'array
(considerando la numerazione delle righe che parte da 0).
Modificare gli elementi selezionati nel primo punto dell'esercizio aggiungendo 10 al loro valore.
"""
import numpy as np

#punto 1
arr = np.random.randint(10, 51, size=(4, 4)) #creazione di un array 4x4 con numeri casuali tra 10 e 50
print("Matrice 4x4:\n", arr)
#punto 2
fancy_index = [(0, 1), (1, 3), (2, 2), (3, 0)] #indici da selezionare
fancy_elements = arr[fancy_index] #selezione degli elementi con fancy indexing
print("Elementi selezionati con fancy indexing:", fancy_elements)
#punto 3
odd_rows = arr[1::2, :] #selezione di tutte le righe dispari dell'array
print("Righe dispari dell'array:\n", odd_rows)
#punto 4
#ValueError: cannot reshape array of size 41 into shape (4,4)
arr[fancy_index] += 10 #modifica degli elementi selezionati aggiungendo 10
print("Matrice dopo la modifica:\n", arr)