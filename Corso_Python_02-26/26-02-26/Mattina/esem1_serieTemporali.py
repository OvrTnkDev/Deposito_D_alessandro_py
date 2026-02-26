import pandas as pd

# 1. Generazione di una serie temporale con frequenza 'ME' (Month End)
date_range = pd.date_range(start='2026-01-01', periods=10, freq='ME')

# 2. Creazione del DataFrame (Uso 'Valore' come nome colonna)
df = pd.DataFrame({
    'Data': date_range, 
    'Valore': [10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
})

# 3. Fondamentale: impostare la colonna 'Data' come indice per usare resample/rolling
df.set_index('Data', inplace=True)

# Aggiunge una colonna con il valore del mese precedente (Shift)
df['prev_month'] = df['Valore'].shift(1)

# Tasso di variazione mensile (Percent Change)
df['monthly_return'] = df['Valore'].pct_change()

# Finestra mobile di 3 periodi (media e deviazione standard)
# Nota: Uso 3 invece di 7 solo per vedere i dati, dato che abbiamo solo 10 righe
df['rolling_mean3'] = df['Valore'].rolling(window=3).mean()
df['rolling_std3']  = df['Valore'].rolling(window=3).std()

print("DataFrame Analisi Temporale ('ME'):")
print(df)

# --- RESAMPLING ---

# Esempio di resampling giornaliero ('D') partendo dai dati mensili
df_daily = df['Valore'].resample('D').asfreq()

print("\nPrime righe del resampling giornaliero (Upsampling):")
print(df_daily.head(5))