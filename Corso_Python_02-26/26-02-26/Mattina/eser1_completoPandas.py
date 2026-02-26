"""
Obiettivo:
Utilizzare pandas e numpy per esplorare, pulire, trasformare e analizzare un dataset di clienti della compagnia di
telecomunicazioni. L'esercizio mira a costruire un modello predittivo di base per la churn rate e scoprire correlazioni tra
vari attributi del cliente e la loro fedeltà.


Dataset: 
ID_Cliente: Identificativo unico per ogni cliente
Età: Età del cliente
Durata_Abonnamento: Quanti mesi il cliente è stato abbonato
Tariffa_Mensile: Quanto il cliente paga al mese
Dati_Consumati: GB di dati consumati al mese
Servizio_Clienti_Contatti: Quante volte il cliente ha contattato il servizio clienti
Churn: Se il cliente ha lasciato la compagnia (Sì/No)


Caricamento e Esplorazione Iniziale:
Caricare i dati da un file CSV.
Utilizzare info(), describe(), e value_counts() per esaminare la distribuzione dei dati e identificare colonne con
valori mancanti.

Pulizia dei Dati:
Gestire i valori mancanti in modo appropriato, considerando l'imputazione o la rimozione delle righe.
Verificare e correggere eventuali anomalie nei dati (es. età negative, tariffe mensili irrealistiche).

Analisi Esplorativa dei Dati (EDA):
Creare nuove colonne che potrebbero essere utili, come Costo_per_GB (tariffa mensile divisa per i dati consumati).
Utilizzare groupby() per esplorare la relazione tra Età, Durata_Abonnamento, Tariffa_Mensile e la Churn.
Utilizzare metodi come corr() per identificare possibili correlazioni tra le variabili.

Preparazione dei Dati per la Modellazione:
Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì").
Normalizzare le colonne numeriche usando numpy per prepararle per la modellazione.

Analisi Statistica e Predittiva:
Implementare un semplice modello di regressione logistica usando scikit-learn per predire la probabilità di churn basata
su altri fattori.
Valutare la performance del modello attraverso metriche come l'accuratezza e l'AUC (Area Under Curve).
"""

import pandas as pd
import numpy as np


PATH_FILE = r"Corso_Python_02-26/26-02-26/Mattina/database/telecorn_churn.csv"

# # Generazione del dataset con qualche dato mancante e anomalie

# np.random.seed(0)  # Per la riproducibilità
# num_clienti = 1000

# """ 
#     uniform per generare dati consumati tra 1 e 50 GB, con arrotondamento a 2 decimali 
#     e serve per evitare valori troppo alti o troppo bassi che potrebbero essere irrealistici
# """
# data = {
#     #dati generati in modo sequenziale da 1 a 1000 per identificare univocamente ogni cliente
#     # co qualche dato mancante (NaN) per testare la gestione dei dati mancanti
#     'ID_Cliente': np.arange(1, num_clienti + 1),
#     'Età': np.random.randint(18, 70, size=num_clienti),
#     'Durata_Abbonamento': np.random.randint(1, 60, size=num_clienti),
#     'Tariffa_Mensile': np.random.uniform(20, 100, size=num_clienti).round(2),
#     'Dati_Consumati': np.random.uniform(1, 50, size=num_clienti).round(2),
#     'Servizio_Clienti_Contatti': np.random.randint(0, 10, size=num_clienti),
#     'Churn': np.random.choice(['Sì', 'No', np.nan], size=num_clienti, p=[0.2, 0.7, 0.1])  # 20% churn, 70% no churn, 10% dati mancanti
# }

# # Creazione del DataFrame
# df = pd.DataFrame(data)
# print("Dataset Generato:")
# print(df.shape) #mostro la forma del sataset
# print(df.head()) #mostro le prime 5 righe del dataset

# #lo carico in un csv
# df.to_csv(PATH_FILE, index=False)

#carico il dataset da csv
df = pd.read_csv(PATH_FILE)
print("Dataset Caricato:")
print(df.shape) #mostro la forma del sataset
print(df.head()) #mostro le prime 5 righe del dataset
print("\n" +  "=" * 50 + "\n")

#utilizzo info() per esaminare la distribuzione dei dati e identificare colonne con valori mancanti
print("Informazioni sul Dataset:")
print(df.info())
print("\n" +  "=" * 50 + "\n")

#utilizzo describe() per esaminare la distribuzione dei dati numerici
print("Statistiche Descrittive del Dataset:")
print(df.describe())
print("\n" +  "=" * 50 + "\n")

#utilizzo value_counts() per esaminare la distribuzione dei dati categorici (Churn)
print("Distribuzione della Colonna 'Churn':")
print(df['Churn'].value_counts(dropna=False)) #dropna=False per includere i valori mancanti nella conta
print("\n" +  "=" * 50 + "\n")

#creo una nuova colonna Costo_per_GB (tariffa mensile divisa per i dati consumati)
df['Costo_per_GB'] = (df['Tariffa_Mensile'] / df['Dati_Consumati']).round(2)
print("Colonna 'Costo_per_GB' Aggiunta:")
print(df[['Tariffa_Mensile', 'Dati_Consumati', 'Costo_per_GB']].head())
print("\n" +  "=" * 50 + "\n")

#esplorazione tramite groupby()
groupb_df = df.groupby('Churn')[['Età', 'Durata_Abbonamento', 'Tariffa_Mensile']].mean()
print("Media di Età, Durata_Abbonamento e Tariffa_Mensile per Churn:")
print(groupb_df)
print("\n" +  "=" * 50 + "\n")

"""
utilozzo corr() per identificare possibili correlazioni tra le variabili numeriche
La matrice di correlazione mostra i valori di correlazione tra le variabili numeriche del dataset.
I valori di correlazione variano tra -1 e 1, dove:
- Un valore vicino a 1 indica una forte correlazione positiva (le variabili tendono a muoversi nella stessa direzione).
- Un valore vicino a -1 indica una forte correlazione negativa (le variabili tendono a muoversi in direzioni opposte).
- Un valore vicino a 0 indica una debole o nessuna correlazione (le variabili non mostrano una relazione lineare evidente).
"""
correlation_m = df[['Tariffa_Mensile', 'Dati_Consumati', 'Costo_per_GB']].corr()
print("Matrice di Correlazione tra le Variabili Numeriche:")
print(correlation_m)

# Preparazione dei Dati per la Modellazione, ma inizio a normalizzare prima i dati nulli
# Convertire la colonna Churn in formato numerico (0 per "No", 1 per "Sì")
churn_dfNaN = df['Churn'].value_counts(dropna=False)
print("\nConteggio dei Valori nella Colonna 'Churn' Prima della Conversione:")
print(churn_dfNaN)
print("\n" +  "=" * 50 + "\n")

# Converto 'Sì' in 1 e 'No' in 0, lasciando i NaN come sono per ora
df['Churn'] = df['Churn'].map({'No': 0, 'Sì': 1})

#converso Nan facendo la media
df['Churn'] = df['Churn'].fillna(df['Churn'].mean())
print(df['Churn'])
print("\n" +  "=" * 50 + "\n")

#converso in int per vedere se ci sono ancora valori nulli dopo la conversione
df['Churn'] = df['Churn'].astype(int)
print("Colonna 'Churn' Convertita in Numerico:")
print(df['Churn'])
print("\n" +  "=" * 50 + "\n")

#salvo tutto in csv per vedere se ci sono ancora valori nulli dopo la conversione
df.to_csv(r"Corso_Python_02-26/26-02-26/Mattina/database/telecorn_churn_prepared.csv", index=False)
