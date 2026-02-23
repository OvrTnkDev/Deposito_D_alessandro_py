"""Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50.

Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array.
Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing.

Obiettivo:
Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande."""
import numpy as np

arr = np.random.randint(1, 51, size=20) #creazione di un array con 20 numeri casuali tra 1 e 100
print(" Array originale:", arr)

# Slicing di base
arr_sliced = arr[:10]
print(f"Primi 10 elementi: {arr_sliced}")  # Output: primi 10 elementi
arr_sliced2 = arr[-5:]
print(f"ultimi 5 elementi: {arr_sliced2}")  # Output: ultimi 5 elementi
arr_sliced3 = arr[5:15]
print(f"elementi 5-15: {arr_sliced3}")  # Output: elementi 5-15

arr_sliced4 = arr[::3]
print(f"elementi ogni 3 posizioni: {arr_sliced4}")  # Output: elementi ogni 3 posizioni

arr_copy = arr.copy() #creazione di una copia dell'array
arr_copy[5:10] = 99 #modifica di un intervallo di elementi
print(f"Array originale: {arr}")
print(f"Array dopo la modifica: {arr_copy}")