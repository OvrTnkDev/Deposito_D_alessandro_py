import numpy as np

# Creazione di un array NumPy unidimensionale
arr = np.array([1, 2, 3, 4, 5])

# Creazione di un array NumPy bidimensionale
arr2nd = np.array([[1, 2, 3], [4, 5, 6]])

#utilizzo di alcuni metodi e attributi di NumPy per analizzare gli array
print(f"Forma dell'array unidimensionale: {arr.shape}") #output: (5,)
print(f"Numero di dimensioni dell'array unidimensionale: {arr.ndim}") #output: 1

print(f"Forma dell'array bidimensionale: {arr2nd.shape}") #output: (2, 3)
print(f"Numero di dimensioni dell'array bidimensionale: {arr2nd.ndim}") #output: 2

print(f"Tipo di dati dell'array unidimensionale: {arr.dtype}") #output: int64
print(f"Tipo di dati dell'array bidimensionale: {arr2nd.dtype}") #output: int64 

print(f"Numero totale di elementi nell'array unidimensionale: {arr.size}") #output: 5
print(f"Numero totale di elementi nell'array bidimensionale: {arr2nd.size}") #output: 6

print(f"Somma degli elementi dell'array unidimensionale: {arr.sum()}") #output: 15
print(f"Somma degli elementi dell'array bidimensionale: {arr2nd.sum()}") #output: 21

print(f"Media degli elementi dell'array unidimensionale: {arr.mean()}") #output: 3.0
print(f"Media degli elementi dell'array bidimensionale: {arr2nd.mean()}") #output: 3.5

print(f"Valore massimo nell'array unidimensionale: {arr.max()}") #output: 5
print(f"Valore massimo nell'array bidimensionale: {arr2nd.max()}") #output: 6

print(f"Indice dell'elemento massimo nell'array unidimensionale: {arr.argmax()}") #output: 4
print(f"Indice dell'elemento massimo nell'array bidimensionale: {arr2nd.argmax()}") #output: 5


# Creazione di un array con valori da 0 a 9 utilizzando arange
arr2 = np.arange(10) #creazione di un array con valori da 0 a 9
print(f"Array creato con arange: {arr2}") #output: [0

reshap_arr2 = arr2.reshape(2, 5) #ristrutturazione dell'array in una matrice 2x5
print(f"Array ristrutturato in una matrice 2x5: \n{reshap_arr2}") 
#output: [[0 1 2 3 4]
#         [5 6 7 8 9]]