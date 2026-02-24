import numpy as np

#linspace
arr = np.linspace(0, 1, 5) #creazione di un array con 5 valori equidistanti tra 0 e 1
print("Array creato con linspace:", arr)

#random
random_arr = np.random.rand(5, 5) #creazione di un array 5x5 con valori casuali tra 0 e 1
print("Array creato con random:", random_arr.round(2)) #arrotondamento a 2 decimali

#sum, mean, std
print("Somma di tutti gli elementi dell'array random:", random_arr.sum())
print("Somma di tutti gli elementi dell'array random:", np.sum(random_arr))

print("Media di tutti gli elementi dell'array random:", random_arr.mean())
print("Media di tutti gli elementi dell'array random:", np.mean(random_arr))

print("Deviazione standard di tutti gli elementi dell'array random:", random_arr.std())
print("Deviazione standard di tutti gli elementi dell'array random:", np.std(random_arr))