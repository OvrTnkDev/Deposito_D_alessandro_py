"""
Hai 60 minuti per creare un esercizio che rappresenti tutto quello
che hai imparato nella settimana precedente.

abbiamo visto numpy, pandas matplot e seaborn, quindi puoi creare una traccia descrittiva
che coinvolga tutte queste librerie.

Traccia:
- Crea un dataset con numpy, ad esempio 1000 campioni di dati con 4 colonne x
  (ad esempio: età, altezza, peso, reddito) e qualche dato NaN per rendere il dataset più realistico
- Crea un DataFrame con pandas utilizzando il dataset creato x
- Esplora i dati con pandas, ad esempio calcolando la media, la mediana e la
  deviazione standard per ogni colonna x
- Utilizza pandas per pulire i dati, ad esempio rimuovendo le righe con valori NaN o sostituendoli con la media x
- Utilizza matplotlib per creare un grafico a barre che mostri la relazione tra altezza e peso ed eta e reddito
- Utilizza seaborn per creare un grafico a barre che mostri la distribuzione delle età nel dataset
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#creo i dati con numpy
data = {
    'eta': np.random.randint(18, 70, size=1000),
    'altezza': np.random.normal(170, 10, size=1000),
    'peso': np.random.normal(70, 15, size=1000),
    'reddito': np.random.normal(30000, 10000, size=1000)
        }

#aggiungo qualche dato NaN per rendere il dataset più realistico tramite slicng o f indexing
data['altezza'][np.random.choice(1000, 50, replace=False)] = np.nan
data['peso'][np.random.choice(1000, 50, replace=False)] = np.nan

#creo il DataFrame con Pandas e lo mostro con le prime 5 righe e le ultime 5 righe
df = pd.DataFrame(data)
#prime 5 righe
print(df.head())
#ultime 5 righe
print(df.tail())

#do la possibilitá di salvare il dataset in un file csv ma possiamo anche commentarlo se non si vuole salvare
df.to_csv('Corso_Python_02-26/27-02-26/Mattina/database/dataset.csv')

"""
facciamo un po di esplorazione dei dati con pandas,
ad esempio calcolando la media, la mediana e la deviazione standard per ogni colonna
"""

print(f"Informazioni sul dataset:\n{df.info()}")
print("-" * 50)
#calcolo la media, la mediana e la deviazione standard per ogni colonna
print(f"Media Etá sul dataset:\n{df['eta'].mean()}")
print(f"Mediana Etá sul dataset:\n{df['eta'].median()}")
print(f"Deviazione Standard Etá sul dataset:\n{df['eta'].std()}")
print("-" * 50)

print(f"Media Altezza sul dataset:\n{df['altezza'].mean()}")
print(f"Mediana Altezza sul dataset:\n{df['altezza'].median()}")
print(f"Deviazione Standard Altezza sul dataset:\n{df['altezza'].std()}")
print("-" * 50)

print(f"Media Peso sul dataset:\n{df['peso'].mean()}")
print(f"Mediana Peso sul dataset:\n{df['peso'].median()}")
print(f"Deviazione Standard Peso sul dataset:\n{df['peso'].std()}")
print("-" * 50)

print(f"Media Reddito sul dataset:\n{df['reddito'].mean()}")
print(f"Mediana Reddito sul dataset:\n{df['reddito'].median()}")
print(f"Deviazione Standard Reddito sul dataset:\n{df['reddito'].std()}")
print("-" * 50)

#usiamo anche describe per avere una panoramica generale del dataset
print(f"Descrizione del dataset:\n{df.describe()}")
print("-" * 50)

#adesso passiamo alla ricerca dei valori NaN
print(f"Valori NaN per ogni colonna:\n{df.isna().sum()}")
print("-" * 50)

"""
adesso che sappiamo quanti e dove sono i valori NaN, possiamo decidere 
se rimuovere le righe con valori NaN o sostituirli con la media
in questo caso faccio entrami in facendomi una copy del dataset originale
"""
df_cleaned = df.copy()

#rimuovo le righe con valori NaN
df_cleaned = df_cleaned.dropna()
print(f"Dataset dopo aver rimosso le righe con valori NaN:\n{df_cleaned.info()}")
print("-" * 50)

#adesso creo una nuova copia del dataset originale per sostituire i valori NaN con la media
df_filled = df.copy()

#sostituisco i valori NaN con la media
df_filled['altezza'] = df_filled['altezza'].fillna(df_filled['altezza'].mean())
df_filled['peso'] = df_filled['peso'].fillna(df_filled['peso'].mean())
print(f"Dataset dopo aver sostituito i valori NaN con la media:\n{df_filled.info()}")
print("-" * 50)

print(f"Dataset con valori NaN sostituiti con la media:\n{df_filled}")
print("-" * 50)

#faccio una groupby per vedere la media del reddito per ogni fascia di etá
df_filled['eta_group'] = pd.cut(df_filled['eta'], bins=[17, 30, 50, 70], labels=['18-30', '31-50', '51-70'])
income_by_age_group = df_filled.groupby('eta_group')['reddito'].mean()
print(f"Reddito medio per fascia di etá:\n{income_by_age_group}")
print("-" * 50)

#li salviamo giusto anche per una visualizzazione futura
df_cleaned.to_csv('Corso_Python_02-26/27-02-26/Mattina/database/dataset_cleaned.csv')
df_filled.to_csv('Corso_Python_02-26/27-02-26/Mattina/database/dataset_filled.csv')
income_by_age_group.to_csv('Corso_Python_02-26/27-02-26/Mattina/database/income_by_age_group.csv')


"""
abbiamo visto come creare un dataframe da un dataset creato con numpy,
abbiamo fatto un'esplorazione concreta per comprendere se ci sono anomalie o valori mancanti,
e nel caso ci sono stati, abbiamo visto come rimuoverli o sostituirli con la media.
Abbiamo calcolato la media, la mediana e la deviazione standard per ogni colonna,
e abbiamo anche usato describe per avere una panoramica generale del dataset.

Adesso tocca a Matplot e Serabon per la visualizzazione dei dati,
perché come abbiamo detto fino ad oggi, la visualizzazione è una parte fondamentale dell'analisi dei dati.
"""

#uniamo i due grafici in un'unica figura
fig, axes = plt.subplots(2,
                         1,
                         figsize=(12, 8),
                         dpi=100)

# Grafico a barre della relazione tra altezza e peso ed eta e reddito
axes[0].bar(df_filled['altezza'],
                df_filled['peso'],
                label='Altezza vs Peso',
                color='blue',
                alpha=0.5)

axes[0].bar(df_filled['eta'],
                df_filled['reddito'],
                label='Età vs Reddito',
                color='red',
                alpha=0.5)

axes[0].set_title('Grafico a Barre della Relazione tra Altezza e Peso ed Età e Reddito')
axes[0].set_xlabel('Altezza / Età')
axes[0].set_ylabel('Peso / Reddito')
axes[0].legend()
axes[0].grid()

# Grafico a barre della media del reddito per fascia di etá
sns.barplot(x=income_by_age_group.index,
            y=income_by_age_group.values,
            palette='viridis',
            ax=axes[1])

axes[1].set_title('Media Reddito per Fascia di Età')
axes[1].set_xlabel('Fascia di Età')
axes[1].set_ylabel('Media Reddito')
plt.tight_layout()
plt.show()