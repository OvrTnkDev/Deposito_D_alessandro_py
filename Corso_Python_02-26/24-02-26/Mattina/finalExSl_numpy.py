"""Es finale Day One - Consegna

Crea uno script Python che esegua i seguenti passaggi:

Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a 49. più altre 50 posizioni casuali tra 49 e 101.
Stampa l’array, il suo dtype e la sua shape.
Modifica il tipo di dato (dtype) dell’array in float64.
Verifica e stampa di nuovo dtype e shape.
Utilizza lo slicing per ottenere:
i primi 10 elementi
gli ultimi 7 elementi
gli elementi dall’indice 5 all’indice 20 escluso
ogni quarto elemento dell'array
Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso) assegnando loro il valore 999.
Utilizza la fancy indexing per selezionare:
gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
tutti gli elementi pari dell’array utilizzando una maschera booleana
tutti gli elementi maggiori della media dell'array
Stampa:
l’array originale dopo tutte le modifiche
tutti i sotto-array ottenuti tramite slicing e fancy indexin"""
import numpy as np



#punto 1
arr = np.arange(50) #creazione di un array con valori da 0 a 49
random_values = np.random.randint(49, 101, size=50) #creazione di un array con 50 numeri casuali tra 49 e 101
arr = np.concatenate((arr, random_values)) #unione dei due array
print("Array originale:", arr)
print("Dtype:", arr.dtype) #stampa del tipo di dato
print("Shape:", arr.shape) #stampa della forma dell'array

#punto 2
arr = arr.astype(np.float64) #modifica del tipo di dato in float64
print("Dtype dopo modifica:", arr.dtype) #stampa del nuovo tipo di dato
print("Shape dopo modifica:", arr.shape) #stampa della forma dell'array dopo la modifica

#punto 3
first_10 = arr[:10] #primi 10 elementi
last_7 = arr[-7:] #ultimi 7 elementi
elements_5_20 = arr[5:20] #elementi dall'indice 5 all'indice 20 escluso
every_4th = arr[::4] #ogni quarto elemento dell'array
print("Primi 10 elementi:", first_10)
print("Ultimi 7 elementi:", last_7)
print("Elementi dall'indice 5 all'indice 20 escluso:", elements_5_20)
print("Ogni quarto elemento dell'array:", every_4th)

#punto 4
arr_copy = arr.copy() #creazione di una copia dell'array
arr_copy[10:15] = 999 #modifica degli elementi dall'indice 10 a 15 (escluso) assegnando loro il valore 999
print("Array originale dopo la modifica:", arr_copy)

#punto 5 fancy indexing
#cosè la fancy indexing?
"""La fancy indexing è una tecnica di indicizzazione in NumPy che consente di selezionare elementi specifici
da un array utilizzando un array di indici o una maschera booleana.
In questo caso, possiamo utilizzare la fancy indexing per selezionare gli elementi
in posizione [0, 3, 7, 12, 25, 33, 48]"""
index = [0, 3, 7, 12, 25, 33, 48]
array_fancy = arr[index]
print("Elementi in posizione [0, 3, 7, 12, 25, 33, 48]:", array_fancy)

#maschera booleana per selezionare tutti gli elementi pari dell'array
#cosa e una maschera booleanan?
"""Una maschera booleana è un array di valori booleani (True o False) che viene utilizzato per selezionare
elementi specifici da un array più grande. In questo caso, possiamo creare una maschera booleana che identifica
quali elementi dell'array sono pari (cioè, divisibili per 2 senza resto) e poi utilizzare questa maschera per
estrarre solo gli elementi pari dall'array originale. Tipo filter in Python, ma con array NumPy."""
even_elements = arr[arr % 2 == 0]
print("Elementi pari dell'array:", even_elements)

#selezione di tutti gli elementi maggiori della media dell'array
greater_than_mean = arr[arr > arr.mean()] #selezione di tutti gli elementi maggiori della media dell'array
print("Media dell'array:", arr.mean(), "Elementi maggiori della media dell'array:", greater_than_mean)