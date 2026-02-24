"""
Esercizio 1: Somma e Media di Elementi
Creare un array NumPy di 15 elementi contenente numeri casuali compresi tra 1 e 100.
Calcolare e stampare la somma di tutti gli elementi dell'array.
Calcolare e stampare la media di tutti gli elementi dell'array.
"""
import numpy as np

#punto 1
arr = np.random.randint(1, 101, size=15) #creazione di un array con 15 numeri casuali tra 1 e 100
print("Array creato con random:", arr)

#punto 2
sum_arr = np.sum(arr)
print("Somma di tutti gli elementi dell'array:", sum_arr)
#punto 3
mean_arr = np.mean(arr)
print("Media di tutti gli elementi dell'array:", mean_arr)

