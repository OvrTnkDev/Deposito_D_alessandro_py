"""
Esercizio Medio: Normalizzazione dei Dati

Testo dell'esercizio:
Creato un DataFrame pandas con tre colonne: altezza, peso e età di un gruppo
di persone, normalizza i dati di altezza e peso usando la normalizzazione min-
max (ridimensiona i valori in modo che varino tra 0 e 1). 

Assicurati di lasciare inalterata la colonna età; mostra il DataFrame
originale e quello modificato.


Fornisci un codice che:
Carichi il DataFrame (puoi assumere che i dati siano già disponibili in un
DataFrame chiamato df).
Applichi la normalizzazione min-max alle colonne altezza e peso.
Stampa sia il DataFrame originale sia quello modificato per compararli.
"""
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Dati di esempio per il DataFrame 50x3
data = {
    'altezza': [1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80, 1.85, 1.90, 1.95],
    'peso': [60, 65, 70, 75, 80, 85, 90, 95, 100, 105],
    'età': [25, 30, 35, 40, 45, 50, 55, 60, 65, 70]
       }

# Creazione del DataFrame
df = pd.DataFrame(data)
print("DataFrame Originale:")
print(df)

# Normalizzazione min-max per altezza e peso
df_normalized = df.copy()
df_normalized['altezza'] = (df['altezza'] - df['altezza'].min()) / (df['altezza'].max() - df['altezza'].min())
df_normalized['peso'] = (df['peso'] - df['peso'].min()) / (df['peso'].max() - df['peso'].min())
print("\nDataFrame Normalizzato:")
print(df_normalized)

#stampo dataframe originale e normalizzato tramite grafico a barre
plt.figure('Altezza Originale vs Normalizzata')
sns.barplot(x=df['età'], y=df['altezza'], color='blue', alpha=0.5, label='Altezza Originale')
sns.barplot(x=df_normalized['età'], y=df_normalized['altezza'], color='black', alpha=0.5, label='Altezza Normalizzata')

plt.title('Altezza Originale vs Normalizzata')
plt.xlabel('Età')
plt.ylabel('Altezza')

#aggiungo informazioni alla legenda senza barre aggiuntive
plt.axvline(df["altezza"].mean(),
            color='blue',
            linewidth=1,
            label=f'Altezza media: {df["altezza"].mean():.2f} m',
            alpha=0.2)
plt.axvline(df["altezza"].min(),
            color='blue',
            linewidth=1,
            label=f'Altezza minima: {df["altezza"].min():.2f} m',
            alpha=0.2)
plt.axvline(df["altezza"].max(),
            color='blue',
            linewidth=1,
            label=f'Altezza massima: {df["altezza"].max():.2f} m',
            alpha=0.2)

plt.legend()
plt.show()
