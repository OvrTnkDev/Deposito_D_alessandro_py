import pandas as pd

#percorso del file
file_path = r"Corso_Python_02-26/25-02-26/Mattina/SalesRecords.csv"

#caricamento del file in un DataFrame
df = pd.read_csv(file_path)

#le prime righe del DataFrame
print(df.head(3))