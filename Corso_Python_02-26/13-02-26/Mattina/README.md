## Risposte aperte

# 3.Cos'è Python? quali sono le sue caratteristiche, spiegale

- Python è un linguaggio fortemente dinamico, ideato da Van Rossum. Orientato agli oggetti, quindi OOP, ma supporta anche paradigmi come l'imperativo o il funzionale. Linguaggio ad Alto livello interpretato, quindi vicino al linguaggio umano, ma più complesso per il calcolatore e quindi meno comprensibile. Fortemente dinamico perché le variabili possono cambiare di tipo, ma non possono non averne uno. Una delle particolarità funzionale di python è l'indentazione, perché è fondamentale per racchiudere istruzioni snippet o blocchi di codice in più livelli, quindi serve a far capire all'interprete a quale blocco di codice fa parte quell'istruzione.

# 5.Cos'è una collezione? quali abbiamo studiato in Python? Spiega le differenze e fai un esempio di codice di istanziazione

Le collezioni, genericamente possiamo vederle come dei contenitori, permettono di salvare un insieme di dati in un unica variabile. possono essere di 3 tipi: Modificabili, non modificabili e dinamiche.
Parliamo adesso di quelle che conosco, ovvero: Liste, Tuple, insiemi e dizionari.

Le liste sono ordinate, modificabili ed eterogenee quindi possono avere qualsiasi tipo di dato e sono rappresentate dalle parentesi quadre -> list[]
es:
list_name =["Fabio D'alessandro", "Gabriele Carucci", "Stefano Romanelli", "Elisabetta Carella", "Gabriele Giuliani",
"Veronica Veneroso", "Maria Visione", "Mariagrazia Nuzzolese",
"Valero Carìa","Ilaria Cuccaro", "Marco A. De Felicis", "Giovanni Iadalise"]

Le tuple sono anch'esse ordinate, NON sono modificabili (possiamo vederle come delle costanti), possono essere miste e sono rappresentate dalle parentesi tonde -> tuple()
es:
TUPLE_V = ("a", "e", "i", "o", "u")

Gli insiemi sono modificabili, non sono ordinati, e non possono avere più tipi o meglio è fortemente consigliato non farlo e sono rappresentate dalle parentesi graffe -> set{}. Caratteristica di output -> Se presenta duplicati nell'output non verranno mostrati.
es:
set2 = {1,2,3,4,5}

i dizionari sono utili per rappresentare tabelle di db oppure ogetti, la struttura contiene una key che deve essere SEMPRE stringa e un valore di un type che desideriamo e per questo è semi eterogeneo. Il type è dict(), sono ordinati, rappresentati dalle parentesi graffe -> dict{}
es:
studente = {"nome": "Fabio",
"cognome": "D'alessandro",
"età": 27,
"corso": "Python"}

# 7.Cos'è una classe cos'è un oggetto e cosa possono contenere ? Cos'è un metodo speciale, quali consoci descrivili?

- La classe è un modello o mokup o blueprint (possiamo identificarla come ci è più comodo per aiutarci a captare il concetto), e praticamente identifica un oggetto reale, come ad esempio un'auto.
  Sostanzialmente è l'astrazione del mondo reale e di tutti gli oggetti che ci ruotano in torno(real life).
  In python la si identifica con il type class e l'iniziale del nome deve essere sempre maiuscola.
  E' composta da attributi, metodi normali e speciali e a volte anche da altre classi se ce ne il bisogno.

Gli attributi o proprietà sono delle proprietà condivise tra tutti gli oggetti, e quindi rappresentano la classe.
I metodi sono delle funzioni definite nella classe (associate), che comunque a loro volta rappresentano e definiscono l'oggetto nel suo comportamento.
ci sono alcuni metodi speciali come dicevo prima, come **init** ad esempio che serve a creare il costruttore, **str** che è l'equivalente del toString() poi ce ne sono altri come**name** ecc.
poi abbiamo il self che identifica l'istanza dell'oggetto creato.
I metodi speciali possono essere sia vuoti che associati.

# 9.Spiega le tre regole fondamentali, cosa fanno, e fai un ESEMPIO DI CODICE per ognuna

- L'OOP si base su 3 concetti FONDAMENTALI: Incapsulamento, Ereditarietà e Polimorfismo.
  Il pilastro che le mantiene unite è l'astrazione, e se andassimo a togliere l'astrazione che è la regola base l'OOP non esisterebbe.
  L'incapsulamento è la capacità di proteggere il codice(non a livello di sicurezza informatica), quindi le proprietà all'interno di una classe. è in mano al programmatore per il 50% rispetto alla macchina.
  L'ereditarietà, invece, è la capacità di una classe di avere padri o figli, a qui possono ereditare proprietà e metodi. caratteristica fondamentale di python è la multiereditarietà quindi un figlio puo avere tanti padri e viceversa paragonata alla cardinalità di un database relazionale n:m.
  Per ereditare cio che ci serve dalla classe padre solitamente si usa super(). o il nome della classe quando ci sono piu padri.
  Il polimorfismo è la capacità di cambiare forma e/o comportamento ad un elemento x senza cambiare il tipo.

# 12.Cos'è git e cos'è github? Cosa puoi fare con github? (azioni e concetti)

- Git sostanzialmente è una tecnologia, ad esempio il touchscreen sugli smartphone.
  Github è un prodotto, che sfrutta la tecnologia di git, ed è utile in primis per la condivisione dei progetti quindi lavoro di gruppo, che git non permette di fare.
  Poi la cosa fondamentale è la crono storia, con essa possiamo controllare tutto quello che abbiamo fatto ed è possibile fare anche roll back nel caso di errori o problemi alla versione precedente. poi si aggiungo a questo il push che permette di inviare alla repo le modifiche, il brach che permette di creare un ramo parallelo per ogni sviluppatore cosi da non rompere il progetto principale, il pull che permette di prendere le modifiche apportate al progetto e il merge che permette di unire tutte le modifiche apportate da tutti gli sviluppatori nel branch principale, laddove non ci fossero errori conflitti e problemi.

# 14.Cos'è l'astrazione spiegala sia pratica che teorica

- L'astrazione sostanzialmente nasconde i dettagli complessi in dettagli semplici.
  E quindi questo permette al sistema di comprende ciò che l'utente sostanzialmente scrive e implementa in semplicità come ad esempio il print().
  La cosa più importante è che senza di essa non potrebbero esistere ereditarietà incapsulamento e polimorfismo, perchè l'astrazione è il pilastro che mantiene le tre regole unite.

---

## Link meme

# 16.EXTRA: Fai un meme sul corso

- **[MEME](https://imgflip.com/i/ak1dgb)**
<div align="center">
    <img src="meme.jpg" width="100%" alt="Meme" />
</div>

---

# Grazie per la visione
