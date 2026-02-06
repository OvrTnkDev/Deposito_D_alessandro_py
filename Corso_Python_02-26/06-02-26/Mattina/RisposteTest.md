## Risposte aperte

# 3.Cos'è una collezione? Quali conosci e quali caratteristiche hanno?

- Le collezioni, genericamente possiamo vederle come dei contenitori, permettono di salvare un insieme di dati in un unica variabile.
  possono essere di 3 tipi: Modificabili, non modificabili e dinamiche.

Parliamo adesso di quelle che conosco, ovvero: Liste, Tuple ed insiemi.

Le liste sono ordinate, modificabili ed eterogenee quindi possono avere qualsiasi tipo di dato e sono rappresentate dalle parentesi quadre -> list[]

Le tuple sono anch'esse ordinate, NON sono modificabili (possiamo vederle come delle costanti), possono essere miste e sono rappresentate dalle parentesi tonde -> tuple()

Gli insiemi sono modificabili, non sono ordinati, e non possono avere più tipi o meglio è fortemente consigliato non farlo e sono rappresentate dalle parentesi graffe -> set{}. Caratteristica di output -> Se presenta duplicati nell'output non verranno mostrati.

# 5.Cos'è Python? quali caratteristiche ha?

- Python è un linguaggio fortemente dinamico, ideato da Van Rossum(o come si scrive).
  Orientato agli oggetti, quindi OOP, ma supporta anche paradigmi come l'imperativo o il funzionale.
  Linguaggio ad Alto livello interpretato, quindi vicino al linguaggio umano, ma più complesso per il calcolatore e quindi meno comprensibile.
  Fortemente dinamico perché le variabili possono cambiare di tipo, ma non possono non averne uno.
  Una delle particolarità funzionale di python è l'indentazione, perché è fondamentale per racchiudere istruzioni snippet o blocchi di codice in piu livelli, quindi serve a far capire all'interprete a quale blocco di codice fa parte quell'istruzione.

# 7.Cos'è una variabile e da quali parti è definita? Quali categorie e tipi esistono di variabile?

- Le variabili sono dei contenitori composte SEMPRE da 3 parti: Tipo, Nome, Valore.
  Esistono 2 categorie: Basilari, non Basilari.
  Basilari sono i tipi definiti di python, i non basilari possono essere collegamenti esterni (tipo i db) o gli oggetti.
  Come sottocategorie dei Basilari abbiamo i Numerici composti da int e float, i Booleani composti da True e False e le stringhe visto piu come un tipo di dato speciale poichè composti da caratteri e quindi immaginarli come un array di char. Propio per questo le stringhe hanno dei metodi speciali, ovvero metodi funzionali che ci mette a disposizione python.

# 9.Cos'è una funzione? cosa dimostra implicitamente? Quali tipi ne esistono? cosa sono i parametri? e gli argomenti?

- Una funzione è un blocco autonomo di codice che eseguono un'operazione specifica. Serve a rendere il codice leggibile, modulare riutilizzabile e manu-tenibile.
  implicitamente dimostrano l'astrazione.
  Possono essere di 2 tipi: return, non return(void).
  Return quando ci deve appunto ritornare un valore che ci serve, ad esempio un calcolo aritmetico.
  Non return o void, quando non ci serve un valore di ritorno, ad esempio un semplice print.
  Sono composte da: parola chiave (def), nome della funzione (rigorosamente con lettera minuscola), pararametri.
  I parametri sono i nomi usati nella definizione della funzione, gli argomenti invece sono dei valori che iniettiamo alla funzione, e servono a farci restituire o meno le operazione della funzione creata.

# 11.Cos'è SQL e a cosa serve?

- SQL o Structure query lenguage, è un linguaggio di interrogazione.
  Serve a fare richieste al database, le cosiddette Query, per ottenere delle risposte (dati di ritorno dal db).

# 13.Cos'è un operatore? Cosa cambia tra logico e aritmetico? Spiegami quelli che conosci.

- Un operatore è un simbolo che ci permette di fare delle operazioni su dei valori o su delle variabili.
  Il logico sono il riflesso dei ragionamenti umani, l'aritmetico lo dice la parola stessa ci permette di fare delle operazioni matematiche.
  Per i logici abbiamo: AND - OR - NOT
  AND: sarà true solo quando le due condizioni sono entrambe 1(true), altrimenti 0(false)
  OR: sarà true quando almeno una delle condizioni sarà 1(true), altrimenti 0(false)
  NOT: è la logica inversa quindi quando ad esempio l'AND è true(1) per il NOT sarà false(0), e la stessa cosa vale per l'OR.

# 15.Cos'è il controllo di flusso? Quali famiglie abbiamo in questo capo e quali comandi appartengono a queste famiglie?

- Il controllo di flusso è il concetto principale della programmazione moderna, senza di esso sarebbe un macello (soprattutto se usassimo i GOTO-orrore), servono a condizionare la lettura delle richieste.
  Abbiamo 3 categorie: Condizioni - Cicli - Funzioni
  Condizioni: abbiamo i comandi if, elif ed else.
  Cicli: abbiamo i comandi while e for.
  Funzioni: abbiamo il comando def con return o senza come dicevo anche prima.

---

## Esercizi

# 17.Esercizio 1: Condizioni e cicli

- **[Condizioni e cicli](Corso_Python_02-26/06-02-26/Mattina/Condizioni_e_Cicli.py)**

# 18.Esercizio 2: Funzioni e Liste

- **[Funzioni e Liste](Corso_Python_02-26/06-02-26/Mattina/Funzioni_e_Liste.py)**

---

## Link meme

# 20.EXTRA: Fai un meme sul corso

- **[MEME](https://imgflip.com/i/ajf17y)**

---

# Grazie per la visione
