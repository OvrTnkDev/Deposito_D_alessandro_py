"""Crea un array NumPy utilizzando arange e verifica il tipo di dato (dtype) e la forma (shape) dell'array.

Esercizio:

Utilizza la funzione np.arange per creare un array di numeri interi da 10 a 49.
Verifica il tipo di dato dell'array e stampa il risultato.
Cambia il tipo di dato dell'array in float64 e verifica di nuovo il tipo di dato.
Stampa la forma dell'array."""

import numpy as np


arr = np.arange(10, 50) #creazione di un array con valori da 10 a 48
print(f"Tipo di dati dell'array: {arr.dtype}") #output: int64

arr2 = arr.astype(float) #conversione dell'array in float
print(f"Tipo di dati dell'array dopo la conversione: {arr2.dtype}")#output: float64
print(f"Forma dell'array: {arr.shape}") #output: (40,)