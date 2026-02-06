# 💀 SPECIFICHE TECNICHE: PROJECT HELL-DICE 🩸

> **CLASSIFICAZIONE:** TOP SECRET / LIVELLO DEMONE  
> **AUTORE:** Fabio "The Code Butcher" D'alessandro  
> **STATO:** IN ESECUZIONE (PERICOLO DI MORTE)

---

## 1. VISIONE DEL PROGETTO (The Nightmare)

L'obiettivo è creare un simulatore di dadi (Craps-style) che non si limiti a sputare numeri, ma che giudichi l'anima dell'utente. Il software deve girare su terminale, unico luogo dove nessuno può sentirti urlare quando dimentichi un `;` (ah no, è Python, quando sbagli l'indentazione).

Il sistema deve essere un **Loop Infinito di Sofferenza** (`while True`) da cui si può uscire solo con la vittoria, la morte o il comando `exit` (per i codardi).

---

## 2. REQUISITI DI SANGUE (Funzionalità)

### A. Il Motore del Caos (`lanciaBroski`)

Il sistema deve generare due numeri pseudo-casuali da 1 a 6.

- **Tecnologia:** Modulo `random`.
- **Output:** Due ossa digitali lanciate sul tavolo verde marcio del terminale.

### B. Il Giudizio Universale (`controlloBroski`)

Ogni somma dei dadi deve innescare una sentenza immediata:

- **7 o 11 (Natural):** 🟢 **GUDURIA ESTREMA.** Il giocatore vince e il terminale non esplode.
- **2, 3 o 12 (Craps):** 🔴 **FATALITY.** Il giocatore perde arti, dignità e la partita.
- **Tutto il resto:** 🟡 **IL PURGATORIO.** Il giocatore entra nel limbo ("ContinuaBroski") e deve soffrire ancora.

### C. Interfaccia Utente (UI - User Inferno)

Niente GUI per deboli. Solo testo crudo.

- **Colore:** Il sangue deve scorrere. Uso massiccio di `termcolor`. Sfondi rossi (`on_red`), testo bianco accecante, attributi `blink` per indurre crisi epilettiche nei nemici.
- **Input:** Il sistema deve tollerare l'incompetenza dell'utente. Se scrive "sì" con l'accento o "SI" maiuscolo, il codice deve capire e non crashare (usando `.lower()`).

---

## 3. GESTIONE ERRORI (Anti-Stupidità)

Il sistema è _Bulletproof_.

- Se l'utente cerca di colorare una variabile `None` (classico errore da pivello), il sistema ora resiste grazie alla patch applicata dal Senior Dev.
- Se l'utente inserisce comandi a caso, il sistema risponde con sarcasmo passivo-aggressivo prima di chiudere le porte dell'inferno in faccia.

---

## 4. STACK TECNOLOGICO (Le Armi)

| Arma           | Descrizione                        | Livello di Dolore |
| :------------- | :--------------------------------- | :---------------- |
| **Python 3.x** | Il linguaggio del serpente.        | 🐍 Letale         |
| **Termcolor**  | Per dipingere lo schermo di rosso. | 🎨 Gore           |
| **Random**     | Librerie standard per il caos.     | 🎲 Caotico        |

---

## 5. FLUSSO DI GIOCO (The Pipeline of Doom)

1.  **Ingresso:** "Vuoi giocare?" (Scelta: Entra nell'arena o scappa).
2.  **Lancio:** I dadi rotolano. Il destino è segnato.
3.  **Verdetto:**
    - Vittoria -> Gloria.
    - Sconfitta -> Vergogna.
    - Continua -> Loop.
4.  **Persistence:** Ogni risultato viene marchiato a fuoco in una `lista[]` temporanea visibile a comando.
5.  **Uscita:** Solo tramite comando `exit`, accompagnato da insulti finali del sistema.

---

## 6. MANUTENZIONE E FUTURO

- **v2.0 (To Do):** Implementare suoni di ossa che si spezzano ad ogni `PerditoBroski`.
- **v3.0 (To Do):** Se il giocatore perde 10 volte di fila, lo script formatta l'hard disk (scherzo... forse).

> _"Lasciate ogni speranza, o voi ch'indentate."_
