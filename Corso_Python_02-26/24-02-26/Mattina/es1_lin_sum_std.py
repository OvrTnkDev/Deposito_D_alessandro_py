import numpy as np

arr = np.linspace(0, 1, 12)
arr = arr.round(2) #arrotondamento a 2 decimali
print("Array creato con linspace:", arr)

#cambiare forma in 3x4
arr = arr.reshape(3, 4)
print("Array con forma 3x4:", arr)

#generare una matrice 3x4 con valori casuali tra 0 e 1
random_arr = np.random.rand(3,4)
print("Matrice 3x4 con valori casuali tra 0 e 1:", random_arr.round(2))

#calcola e stampa la somma 
print("Somma di tutti gli elementi dell'array:", np.sum(arr))
print("Somma di tutti gli elementi dell'array random:", np.sum(random_arr.round(2)))