import numpy as np

arr = np.array([1,2,3,4])
scalar = 10

# broadcasting aggiunge lo scalare a ogni elemento dell'array
result = arr + scalar
print("Risultato del broadcasting:", result)    