"""
Parte UNO: Scrivere un Sistema che utilizza NumPy per gestire una matrice 2D. 

Il programma deve presentare un menu interattivo che consente all'utente di eseguire varie operazioni
sulla matrice. Le operazioni disponibili includono, ogni volta che il sistema conclude un calcolo va
salvato su un file txt:

Creare una nuova matrice 2D di dimensioni specificate da utente con numeri casuali.
Estrarre e stampare la sotto-matrice centrale.
Trasporre la matrice e stamparla.
Calcolare e stampare la somma di tutti gli elementi della matrice.
Uscire dal programma o ripetere .


Parte DUE: Andare a specializzare per aggiungere nuove operazioni:

Moltiplicazione Element-wise con un'altra Matrice: L'utente può scegliere di creare 
una seconda matrice delle stesse dimensioni della prima e moltiplicarle elemento per elemento e stampare
il risultato.
Calcolo della Media degli Elementi della Matrice: Calcolare e stampare la media di tutti gli elementi
della matrice.
"""
import numpy as np

while True:
    r = input("Inserisci il numero di righe della matrice (o 'exit' per uscire): ")
    c = input("Inserisci il numero di colonne della matrice (o 'exit' per uscire): ")
    
    if r.lower() == 'exit' or c.lower() == 'exit':
        print("Uscita dal programma.")
        break
    
    try:
        r = int(r)
        c = int(c)
        if r <= 0 or c <= 0:
            print("Per favore, inserisci numeri positivi.")
            continue
    except ValueError:
        print("Per favore, inserisci numeri validi.")
        continue
    
    #creazione matrice 2D con numeri casuali
    matrice = np.random.randint(1, 101, size=(r, c))
    print("Matrice generata:\n", matrice)
    
    # Sotto-matrice centrale
    #perche 4? perche 4 e' la dimensione minima per avere una sotto matrice centrale di almeno 2x2
    start_row = r // 4
    end_row = r - start_row
    start_col = c // 4
    end_col = c - start_col
    sotto_matrice = matrice[start_row:end_row, start_col:end_col]
    print("Sotto-matrice centrale:\n", sotto_matrice)
    
    #trasposizione della matrice
    # trasporre vuol dire scambiare righe e colonne, quindi la prima riga diventa la prima colonna, 
    # la seconda riga diventa la seconda colonna, e così via.
    #con T si ottiene la trasposizione di una matrice, quindi se matrice è una matrice 2D, matrice.T
    # restituirà la matrice trasposta.
    
    trasposta = matrice.T
    print("Matrice trasposta:\n", trasposta)
    
    #calcolo e stampo somma di tutti gli elementi della matrice
    somma = np.sum(matrice)
    print("Somma di tutti gli elementi della matrice:", somma)
    
    #---------- PARTE 2 ---------- 
    
    #moltiplicazione element-wise con un'altra matrice
    scelta = input("Vuoi creare una seconda matrice per la moltiplicazione element-wise? (sì/no): ")
    if scelta.lower() == 'sì':
        matrice2 = np.random.randint(1, 101, size=(r, c))
        print("Seconda matrice generata:\n", matrice2)
        moltiplicazione = matrice * matrice2
        print("Risultato della moltiplicazione element-wise:\n", moltiplicazione)
    
    #calcolo e stampo media di tutti gli elementi della matrice
    media = np.mean(matrice)
    print("Media di tutti gli elementi della matrice:", media)
    
    #---------- PARTE 2 ---------- 
    
    
    #--------- EXTRA ----------
    
    #Determinante della Matrice: Calcolare e stampare il determinante della matrice (solo se la matrice è quadrata).
    if r == c:
        det = np.linalg.det(matrice)
        print("Determinante della matrice:", det)
    
    #--------- EXTRA ----------
    
    #salvataggio su file
    with open(r"Corso_Python_02-26/24-02-26/Pomeriggio/risultati_matrice.txt", "a") as f:
        f.write(f"Matrice originale:\n{matrice}\n")
        f.write(f"Sotto-matrice centrale:\n{sotto_matrice}\n")
        f.write(f"Matrice trasposta:\n{trasposta}\n")
        f.write(f"Somma di tutti gli elementi della matrice: {somma}\n")
        if scelta.lower() == 'sì':
            f.write(f"Seconda matrice:\n{matrice2}\n")
            f.write(f"Risultato della moltiplicazione element-wise:\n{moltiplicazione}\n")
        f.write(f"Media di tutti gli elementi della matrice: {media}\n")
        if r == c:
            f.write(f"Determinante della matrice: {det}\n")