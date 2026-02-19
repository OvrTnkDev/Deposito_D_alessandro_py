## Progetto  Weather API
In questo progetto, utilizzeremo l'API di Open-Meteo per ottenere informazioni meteorologiche su una città specifica. L'utente potrà inserire il nome della città e il numero di giorni per cui desidera ottenere le previsioni meteorologiche. Il programma restituirà le previsioni per i giorni richiesti, inclusi temperatura, velocità del vento e precipitazioni.

### Requisiti
- Python 3.x
- Libreria `requests` per effettuare richieste HTTP
- Libreria `termcolor` per colorare l'output (opzionale)

### Passaggi per l'implementazione
1. Importare le librerie necessarie.
2. Creare un ciclo infinito per permettere all'utente di inserire più città senza dover riavviare il programma.
3. Richiedere all'utente di inserire il nome della città e il numero di giorni per le previsioni.
4. Effettuare una richiesta all'API di Open-Meteo per ottenere le coordinate della città.
5. Utilizzare le coordinate per effettuare una seconda richiesta all'API e ottenere le previsioni meteorologiche.
6. Estrarre le informazioni rilevanti dalle risposte dell'API e stamparele in un formato leggibile.
7. Gestire eventuali errori, come città non trovata o problemi di connessione.
