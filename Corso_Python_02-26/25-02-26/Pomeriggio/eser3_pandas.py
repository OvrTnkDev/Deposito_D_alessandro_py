"""
Esercizio 1: Analisi di Vendite Fittizie


Obiettivo: Utilizzare pandas per analizzare un set di dati di vendite
generato casualmente, applicando le tecniche di pivot e groupby.


Descrizione: Gli studenti dovranno generare un DataFrame di vendite che
include i seguenti campi: "Data", "Città", "Prodotto" e "Vendite". I dati
devono essere generati per un periodo di un mese, con vendite registrate
per tre diverse città e tre tipi di prodotti.


Generazione dei Dati: Utilizzare numpy per creare un set di dati
casuali.

Creazione della Tabella Pivot: Creare una tabella pivot per analizzare
le vendite medie di ciascun prodotto per città.

Applicazione di GroupBy: Utilizzare il metodo groupby per calcolare le
vendite totali per ogni prodotto.
"""

import pandas as pd
import numpy as np

# Generazione dei dati casuali
np.random.seed(0)  # Per la riproducibilità
date_range = pd.date_range(start='2026-01-01', end='2026-01-31', freq='D') #freq D per generare una data al giorno
cities = ['Roma', 'Milano', 'Napoli']
products = ['Mouse', 'Tastiera', 'Monitor']

#creazione del DataFrame con dati casuali inserisco anche l'index
data = {
    'Index': np.arange(1, 101),
    'Data': np.random.choice(date_range, size = 100),
    'Città': np.random.choice(cities, size = 100),
    'Prodotto': np.random.choice(products, size = 100),
    'Vendite': np.random.randint(1, 500, size = 100)
        }
#creazione esplicita del DataFrame con l'index
df = pd.DataFrame(data)
print("DataFrame Originale:")
print(df)
print("\n" + "-"*60 + "\n")


#creo la tabella pivot per analizzare le vendite medie di ciascun prodotto per città
pivot_df = df.pivot_table(values = 'Vendite', index = 'Città', columns='Prodotto', aggfunc='mean')
pivot_df = pivot_df.round(2)  # Arrotondamento a 2 decimali
print("Tabella Pivot:")
print(pivot_df)
print("\n" + "-"*60 + "\n")

#appico il groupby per calcolare le vendite totali per ogni prodotto
group_df = df.groupby('Prodotto')['Vendite'].sum().reset_index()
print("Vendite Totali per Prodotto:")
print(group_df)
print("\n" + "-"*60 + "\n")