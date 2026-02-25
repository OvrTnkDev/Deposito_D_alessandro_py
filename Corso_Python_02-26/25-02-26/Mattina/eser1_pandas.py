"""Esercizio 1: Analisi Esplorativa dei Dati

Obiettivo: Familiarizzare con le operazioni di base per l'esplorazione dei dati
usando pandas.


Dataset: Utilizzare un dataset di esempio che include le seguenti informazioni su
un gruppo di persone: Nome, Età, Città e Salario. 


Caricare i dati in un DataFrame autogenerandoli casualmente .

Visualizzare le prime e le ultime cinque righe del DataFrame.

Visualizzare il tipo di dati di ciascuna colonna.

Calcolare statistiche descrittive di base per le colonne numeriche (media,
mediana, deviazione standard).

Identificare e rimuovere eventuali duplicati.

Gestire i valori mancanti sostituendoli con la mediana della rispettiva
colonna.

Aggiungere una nuova colonna chiamata "Categoria Età" che classifica le
persone come "Giovane", "Adulto" o "Senior" basandosi sull'età (es., 0-18
anni: Giovane, 19-65 anni: Adulto, oltre 65 anni: Senior).

Salvare il DataFrame pulito in un nuovo file CSV."""
import numpy as np
import pandas as pd

#creazione di un dataset di esempio con dati casuali 20x4
#ValueError: All arrays must be of the same length, quindi aggiungo altri 10 nomi, età, città e salari per raggiungere 20 righe

data = {
        'Nome': ['Alice', 'Bob', 'Carla', 'David', 'Eva', 'Francesco', 'Giulia',
                 'Luca', 'Marta', 'Simone', 'Andrea', 'Federica', 'Giorgio', 'Laura', 'Marco', 'Sara',
                 'Stefano', 'Valentina', 'Matteo', 'Chiara'],
        'Età': [17, 30, np.nan, 16, 35, 28, 32, 40, 27, 31, 29, np.nan, 38, 33, 24, 41, 36, 66, 27, 69],
        'Città': ['Roma', 'Milano', 'Napoli', 'Torino', 'Firenze', 'Bologna', 'Genova', 'Venezia',
                  'Verona', 'Padova', 'Trieste', 'Perugia', 'Cagliari', 'Ancona', 'Pescara', 'Reggio Calabria',
                  'Salerno', 'L\'Aquila', 'Catanzaro', 'Potenza'],
        'Salario': [30000, 35000, 28000, 45000, 40000, 32000, 37000, 42000, 31000, 33000, 29000, 31000, 36000,
                    41000, 35555, 38888, 44444, 39999, 32222, 35555]
       }


#inizializzo il dataset in un DataFrame
df = pd.DataFrame(data)
print("DataFrame Originale (prime 5 righe):")
#visualizzo le prime 5 righe del DataFrame con il metodo head()
print(df.head(5))
print("\n" + "-"*60 + "\n")
print("\nDataFrame Originale (ultime 5 righe):")
#visualizzo le ultime 5 righe del DataFrame con il metodo tail()
print(df.tail(5))
print("\n" + "-"*60 + "\n")

#visualizzo il tipo di dati di ciascuna colonna
print("\nTipo di dati di ciascuna colonna:")
print(df.dtypes)
print("\n" + "-"*60 + "\n")

#calcolo statistiche descrittive di base per le colonne numeriche
print("\nStatistiche descrittive per le colonne numeriche:")
"""
utilizzo il metodo describe() per ottenere le statistiche descrittive
che sono media, mediana, deviazione standard, min, max e quartili
Nota: describe() calcola la mediana come 50% percentile, quindi è inclusa nelle statistiche descrittive.
count: numero di valori non nulli
mean: media
std: deviazione standard
min: valore minimo

il quartile e' un valore che divide i dati in quattro parti uguali, quindi:
25%: primo quartile che e' il valore che separa il 25% dei dati più piccoli dal resto
50%: mediana (secondo quartile) che e' il valore che separa i dati in due metà, con il 50% dei dati più piccoli e il 50% dei dati più grandi
75%: terzo quartile che e' il valore che separa il 75% dei dati più piccoli dal resto

max: valore massimo
"""
print(df.describe())
print("\n" + "-"*60 + "\n")

# Rimozione dei duplicati
df = df.drop_duplicates()
print("\nDataFrame dopo la rimozione dei duplicati:")
print(df)
print("\n" + "-"*60 + "\n")

#gestione dei valori mancanti sostituendoli con la mediana della rispettiva colonna
#calcolo la mediana della colonna 'Età' ignorando i valori mancanti
df_none = df.isnull().sum()
print("\nValori mancanti per colonna:")
print(df_none)
print("\n" + "-"*60 + "\n")

#sappiamo che i nulli sono solo in eta, quindi calcoliamo la mediana di eta ignorando i nulli
median_age = df['Età'].median()
print("\nMediana dell'età (ignorando i valori mancanti):", median_age)
#sostituiamo i valori mancanti con la mediana
df['Età'] = df['Età'].fillna(median_age)

#aggiunta di una nuova colonna Categoria Età
#df['Categoria Età'] = df['Età'].apply(lambda x: 'Giovane' if x <= 18 else 'Adulto' if x <= 65 else 'Senior')

#utilizzo pd.cut() per classificare le persone in categorie di età
#pd.cut() fa tipo da ranking, quindi assegna un'etichetta a ciascun intervallo di età definito nei bins
#pd.cut() è una funzione che consente di segmentare e ordinare i valori in bin (intervalli).
df['Categoria Età'] = pd.cut(df['Età'], bins=[0, 18, 65, np.inf], labels=['Giovane', 'Adulto', 'Senior'])

print("\nDataFrame con la nuova colonna 'Categoria Età':")
print(df)
print("\n" + "-"*60 + "\n")

#vado a salvare il DataFrame pulito in un nuovo file CSV
df.to_csv('Corso_Python_02-26/25-02-26/Mattina/data/data_cleaned.csv')
print("\nDataFrame pulito salvato in 'data_cleaned.csv'")