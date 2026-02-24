"""
Esercizio 2: Manipolazione di Array Multidimensionali
Creare una matrice 5x5 contenente numeri interi sequenziali da 1 a 25.
Estrarre e stampare la seconda colonna della matrice.
Estrarre e stampare la terza riga della matrice.
Calcolare e stampare la somma degli elementi della diagonale principale della matrice.
"""
import numpy as np

#punto 1
arr = np.arange(1, 26).reshape(5, 5)
print("Matrice 5x5:\n", arr)
#punto 2
column_2 = arr[:, 1] #seconda colonna
print("Seconda colonna:", column_2)
#punto 3
row_3 = arr[2, :] #terza riga
print("Terza riga:", row_3)
#punto 4
diagonal_sum = np.trace(arr) #somma degli elementi della diagonale principale
print("Somma degli elementi della diagonale principale:", diagonal_sum)