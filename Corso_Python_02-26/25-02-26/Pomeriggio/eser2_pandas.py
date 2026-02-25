"""
Esercizio 2: Manipolazione e Aggregazione dei Dati


Obiettivo: Approfondire le capacità di manipolazione e aggregazione dei dati con
pandas.


Dataset: Utilizzare un dataset che registra le vendite di prodotti in diverse
città, includendo le colonne Prodotto, Quantità, Prezzo Unitario e Città.


Caricare i dati in un DataFrame.

Aggiungere una colonna "Totale Vendite" che sia il risultato del prodotto tra
Quantità e Prezzo Unitario.

Raggruppare i dati per Prodotto e calcolare il totale delle vendite per
ciascun prodotto.

Trovare il prodotto più venduto in termini di Quantità.

Identificare la città con il maggior volume di vendite totali.

Creare un nuovo DataFrame che mostri solo le vendite superiori a un certo
valore (es., 1000 euro).

Ordinare il DataFrame originale per la colonna "Totale Vendite" in ordine
decrescente.

Visualizzare il numero di vendite per ogni città.
"""

import pandas as pd

#creazione del dataset di esempio con dati casuali 20x4
# data = {
#         'Prodotto': ['Laptop', 'Smartphone', 'Tablet', 'Monitor', 'Stampante', 'Mouse', 'Tastiera', 'Cuffie',
#                      'Webcam', 'Speaker', 'Hard Disk', 'Chiavetta USB', 'Router', 'Switch',
#                      'Altoparlante Bluetooth', 'Caricatore', 'Power Bank', 'Smartwatch', 'Action Camera',
#                      'Drone'],
#         'Quantità': [5, 10, 7, 3, 4, 15, 12, 8, 6, 9, 11, 14, 2, 1, 4, 6, 3, 2, 1, 1],
#         'Prezzo Unitario': [800, 600, 300, 200, 150, 50, 70, 120, 90, 110, 100, 40, 60, 30, 200, 25, 40,
#                             150, 250, 500],
#         'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Firenze', 'Bologna', 'Genova', 'Venezia',
#                   'Verona', 'Padova', 'Trieste', 'Perugia', 'Cagliari', 'Ancona', 'Pescara', 'Reggio Calabria',
#                   'Salerno', 'L\'Aquila', 'Catanzaro', 'Potenza']
#        }

data = pd.read_csv('Corso_Python_02-26/25-02-26/Pomeriggio/data/data_vendite.csv')

df = pd.DataFrame(data)
print("DataFrame Originale:")
print(df)
print("\n" + "-"*60 + "\n")

#aggiungo una colonna che calcola il totale delle vendite per ogni riga
df['Totale Vendite'] = df['Quantità'] * df['Prezzo Unitario']
print("DataFrame con la colonna 'Totale Vendite':")
print(df)
print("\n" + "-"*60 + "\n")

#raggruppo i dati per prodotto e calcolo il totale delle vendite per ciascun prodotto
v_per_prodotto = df.groupby('Prodotto')['Totale Vendite'].sum()
print("Totale Vendite per Prodotto:")
print(v_per_prodotto)
print("\n" + "-"*60 + "\n")

#cerco il prodotto piu venduto tramite le quantita'
id_piu_venduto = df['Quantità'].idxmax() #idxmax() restituisce l'indice del valore massimo nella colonna Quantità
p_piu_venduto = df.loc[id_piu_venduto, 'Prodotto'] #loc[] permette di accedere a un elemento specifico del DataFrame usando l'indice
q_piu_venduto = df.loc[id_piu_venduto, 'Quantità']
print(f"Il prodotto più venduto in termini di Quantità ha venduto: {q_piu_venduto} unità di {p_piu_venduto}.")
print("\n" + "-"*60 + "\n")

#vendite solo superiori a 1000 euro
df_superiori_1000 = df[df['Totale Vendite'] > 1000]
print("DataFrame con vendite superiori a 1000 euro:")
print(df_superiori_1000)
print("\n" + "-"*60 + "\n")

#ordino il DataFrame originale per la colonna "Totale Vendite" in ordine decrescente
order_df = df.sort_values(by='Totale Vendite', ascending=False)
print("DataFrame originale ordinato per Totale Vendite in ordine decrescente:")
print(order_df)
print("\n" + "-"*60 + "\n")

#visualizzo il numero di vendite per ogni città
v_per_citta = df.groupby('Città')['Totale Vendite'].sum()
print("Totale Vendite per Città:")
print(v_per_citta)
print("\n" + "-"*60 + "\n")

#salvo le viste nei csv 
# df.to_csv('Corso_Python_02-26/25-02-26/Pomeriggio/data/data_vendite.csv')
v_per_prodotto.to_csv('Corso_Python_02-26/25-02-26/Pomeriggio/data/vendite_per_prodotto.csv')
df_superiori_1000.to_csv('Corso_Python_02-26/25-02-26/Pomeriggio/data/vendite_superiori_1000.csv')
order_df.to_csv('Corso_Python_02-26/25-02-26/Pomeriggio/data/data_ordinato_per_vendite.csv')
v_per_citta.to_csv('Corso_Python_02-26/25-02-26/Pomeriggio/data/vendite_per_citta.csv')
