import numpy as np


# arr = np.array([1, 2, 3, 4, 5])

# # Indexing
# print(arr[0])  # Output: 1
# # Slicing
# print(arr[1:3])  # Output: [2 3]

# # Boolean Indexing
# print(arr[arr > 2])  # Output: [3 4 5]


# arr_2d = np.array([[1, 2, 3, 4],
#                    [5, 6, 7, 8],
#                    [9, 10, 11, 12]])

# # Slicing sulle righe
# print(arr_2d[1:3])  # Output: [[ 5  6  7  8]

#                    #          [ 9 10 11 12]]

# # Slicing sulle colonne
# print(arr_2d[:, 1:3])  # Output: [[ 2  3]
#                        #          [ 6  7]
#                        #          [10 11]]

# # Slicing misto
# print(arr_2d[1:3, 1:3])  # Output: [[ 6  7]
#                         #          [10 11]]


"""Slicing è una tecnica utilizzata per estrarre una parte di un array o di una sequenza. 
In NumPy, lo slicing è simile a quello delle liste in Python, ma è molto più potente e versatile. 
Consente di ottenere subarray di un array esistente senza copiare i dati, il che è efficiente in termini di memoria.

 La sintassi base per lo slicing in NumPy è:


array[start:stop:step]

start: L'indice di inizio dello slicing (inclusivo). Se omesso, il valore predefinito è 0.
stop: L'indice di fine dello slicing (esclusivo). Se omesso, il valore predefinito è la dimensione dell'array.
step: Il passo tra un indice e l'altro. Se omesso, il valore predefinito è 1."""
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7])  # Output: [2 3 4 5 6]


# Slicing con passo
print(arr[1:8:2])  # Output: [1 3 5 7]


# Omettere start e stop
print(arr[:5])  # Output: [0 1 2 3 4]
print(arr[5:])  # Output: [5 6 7 8 9]


# Utilizzare indici negativi
print(arr[-5:])  # Output: [5 6 7 8 9]
print(arr[:-5])  # Output: [0 1 2 3 4]



"""Fancy indexing è una tecnica che permette di selezionare elementi di un array utilizzando array
di indici interi.
Questo consente una selezione complessa e flessibile di elementi rispetto allo slicing normale."""
arr = np.array([10, 20, 30, 40, 50])

# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr[indices])  # Output: [20 40]

# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr[indices])  # Output: [10 30 50]