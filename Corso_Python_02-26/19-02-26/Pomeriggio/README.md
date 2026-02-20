# PokéDex Python Simulator

Questo progetto è un simulatore di **PokéDex** sviluppato in Python. Il programma interagisce con le [PokeAPI](https://pokeapi.co/) per permettere all'utente di incontrare, catturare e catalogare i Pokémon in un database locale.

## 📌 Descrizione del Progetto

Il software simula l'esperienza di un allenatore Pokémon attraverso un'interfaccia a riga di comando (CLI). Quando viene incontrato un Pokémon, il sistema verifica se è già presente nel database `pokedex.json`. In caso di nuovo incontro, viene calcolata una probabilità di cattura; se ha successo, le caratteristiche principali del Pokémon vengono salvate permanentemente.

## 🛠️ Funzionalità Principali

- **Incontro Casuale:** Generazione di un ID random (da 1 a 1025) per trovare un Pokémon selvatico.
- **Ricerca per Numero:** Possibilità di cercare un Pokémon specifico tramite il suo identificativo nazionale.
- **Gestione Database (JSON):** \* Lettura e scrittura automatica su file `pokedex.json`.
  - Verifica dei duplicati per evitare di catturare lo stesso Pokémon più volte.
- **Dati Salvati:** Per ogni cattura vengono archiviati:
  - Nome e ID ufficiale.
  - Altezza e Peso.
  - Tipi (es. Grass, Poison).
  - Abilità.

## 🚀 Requisiti e Installazione

Il programma richiede Python 3.10 o superiore e la libreria `requests`.

1.  **Installazione dipendenze:**

    ```bash
    pip install requests
    ```

2.  **Configurazione Percorso:**
    Assicurati che la cartella definita nella variabile `FILE_NAME` esista, oppure modificala per salvare il file nella cartella principale:

    ```python
    FILE_NAME = "pokedex.json"
    ```

3.  **Esecuzione:**
    ```bash
    python main.py
    ```

## 📂 Struttura del Codice

Il codice è organizzato in funzioni modulari per facilitarne la manutenzione:

- `get_pokemon(num)`: Gestisce la chiamata API e il recupero dei dati grezzi.
- `pokemon_info(pokemon)`: Filtra solo le informazioni necessarie per il salvataggio.
- `check_pokedex()`: Controlla la presenza del Pokémon nel file locale.
- `append_pokedex()`: Gestisce l'aggiornamento del file JSON senza sovrascrivere i dati esistenti.

---

_Progetto realizzato per il corso di Python e Machine Learning._
