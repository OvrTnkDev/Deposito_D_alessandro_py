import numpy as np


#creazione di una matrice quadrata
A = np.array([[1, 2], [4, 5]])
print("Matrice A:\n", A)

#calcolo dell'inversa di A
A_inv = np.linalg.inv(A)
print("Inversa di A:\n", A_inv)

#norma di un vettore
"""La norma di un vettore è una misura della sua lunghezza o grandezza.
Esistono diversi tipi di norme, ma la più comune è la norma euclidea (o L2),
che si calcola come la radice quadrata della somma dei quadrati dei suoi componenti."""
v = np.array([3,4])
norm_v = np.linalg.norm(v)
print("Norma del vettore v:", norm_v)

#creazione della matrice A e del vettore B
A = np.array([[3,1], [1, 2]])
B = np.array([9, 8])

#risoluzione del sistema di equazioni lineari Ax = B
x = np.linalg.solve(A, B)
print("Soluzione del sistema di equazioni lineari Ax = B:", x)

#creazione di un segnale
t = np.linspace(0, 1, 400) #creazione di un array di 400 valori equidistanti tra 0 e 1
signal = np.sin(2 * np.pi * 5 * t) + np.sin(2 * np.pi * 120 * t) #creazione di un segnale che è la somma di due sinusoidi
print("Segnale creato:", signal)

#calcolo della traformata di fourier
fft_sign = np.fft.fft(signal)
print("Trasformata di Fourier del segnale:", fft_sign)

#frequenze associate
freqs = np.fft.fftfreq(len(fft_sign))

print("Trasformazione di Fourier del segnale:", fft_sign)
print("Frequenze associate:", freqs)