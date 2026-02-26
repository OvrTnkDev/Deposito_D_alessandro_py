"""
Esercizio Facile: Calcolo di Statistiche di Base

Testo dell'esercizio:
Hai a disposizione un dataset, che devi autogenerare,
contenuto in un DataFrame pandas con una singola colonna
temperature che rappresenta la temperatura giornaliera in
una città per un mese. 

Scrivi un programma Python che calcoli e stampi le seguenti
statistiche:
La temperatura massima
La temperatura minima
La temperatura media
La mediana delle temperature
"""
import matplotlib.pyplot as plt
import numpy as np

# Genera 30 temperature giornaliere con una distribuzione normale da -6 a 35 gradi Celsius
# loc è la media, scale è la deviazione standard, size è il numero di campioni
data = np.random.normal(loc=20, scale=5, size=30).round(1)

#temperatura massima
temp_max = np.max(data)
temp_min = np.min(data)
temp_mean = np.mean(data)
temp_median = np.median(data)

#instogramma
plt.figure('Istogramma Temperature')
plt.hist(data, bins=30, edgecolor='orange', color='brown')
plt.title('Istogramma delle Temperature')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Giorni')
plt.axvline(temp_min, color='purple',
            linestyle='dashed', linewidth=1,
            label=f'Temperatura Minima: {temp_min:.1f}°C',
            alpha=0.5)
plt.axvline(temp_max,
            color='green',
            linestyle='dashed',
            linewidth=1,
            label=f'Temperatura Massima: {temp_max:.1f}°C',
            alpha=0.5)
plt.axvline(temp_mean,
            color='red',
            linestyle='dashed',
            linewidth=1,
            label=f'Media: {temp_mean:.1f}°C',
            alpha=0.5)
plt.axvline(temp_median,
            color='blue',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana: {temp_median:.1f}°C',
            alpha=0.5)
plt.legend()
plt.show()



#scatter plot
x = np.arange(1, 31)  # Giorni del mese da 1 a 30
y = data  # Temperature generate


plt.figure('Scatter Plot Temperature')
plt.scatter(x, y, color='blue')
plt.title('Scatter Plot delle Temperature')
plt.xlabel('Giorno del Mese')
plt.ylabel('Temperatura (°C)')
plt.axvline(temp_min, color='purple',
            linestyle='dashed', linewidth=1,
            label=f'Temperatura Minima: {temp_min:.1f}°C',
            alpha=0.5)
plt.axvline(temp_max,
            color='green',
            linestyle='dashed',
            linewidth=1,
            label=f'Temperatura Massima: {temp_max:.1f}°C',
            alpha=0.5)
plt.axvline(temp_mean,
            color='red',
            linestyle='dashed',
            linewidth=1,
            label=f'Media: {temp_mean:.1f}°C',
            alpha=0.5)
plt.axvline(temp_median,
            color='blue',
            linestyle='dashed',
            linewidth=1,
            label=f'Mediana: {temp_median:.1f}°C',
            alpha=0.5)
plt.legend()
plt.show()