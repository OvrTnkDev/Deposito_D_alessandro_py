"""Classe MembroSquadra:

Attributi:
nome (stringa) (ok)
età (intero) (ok)
Metodi:
descrivi() (stampa una descrizione generale del membro della squadra) (ok)

Classi Derivate:
Giocatore:

Attributi aggiuntivi come ruolo (e.g., attaccante, difensore) e numero_maglia (ok)
Metodi come gioca_partita() che possono includere azioni specifiche del giocatore (ok)

Allenatore: 
Attributi aggiuntivi come anni_di_esperienza
Metodi come dirige_allenamento() che dettagliano come l'allenatore conduce gli allenamenti
Assistente:
Attributi aggiuntivi come specializzazione (e.g., fisioterapista, analista di gioco)
Metodi specifici del ruolo, come supporta_team() che può descrivere varie forme di supporto al team

Crea due squadre e falle giocare contro."""

import random as rnd

# classe base per i membri della squadra
class MembroSquadra():
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta
        
    def __str__(self):
        return f"{self.nome}, {self.eta} anni"

# classe derivata per i giocatori
class Giocatore(MembroSquadra):
    def __init__(self, nome, eta, ruolo, numero_maglia):
        super().__init__(nome, eta)
        self.ruolo = ruolo
        self.numero_maglia = numero_maglia
        
    # metodo per simulare una partita giocata dal giocatore
    def gioca_partita(self):
        # definisco un dizionario con le azioni possibili per ogni ruolo e le relative probabilità
        azioni = {"attaccante": {"azione": {"segna gol": 0.7, "passa palla": 0.2, "perde palla": -0.1}},
                "difensore": {"azione": {"intercetta palla": 0.6, "passa palla": 0.3, "perde palla": -0.5}},
                "centtrocampista": {"azione": {"passa palla": 0.5, "segna gol": 0.3, "perde palla": -0.2}}}
        # scelgo l'azione in base al ruolo del giocatore e alle probabilità definite nel dizionario
        for ruolo in azioni.keys():
            if self.ruolo == ruolo:
                for azione in azioni[ruolo]["azione"].keys():
                    if rnd.random() < azioni[ruolo]["azione"][azione]:
                        return f"{self.nome} {azione}!"
        return f"{self.nome} è coglion*."

class Allenatore(MembroSquadra):
    def __init__(self, nome, eta, anni_di_esperienza = 0.1):
        super().__init__(nome, eta)
        self.anni_di_esperienza = anni_di_esperienza
        
        
class Assistente(MembroSquadra):
    def __init__(self, nome, eta, specializzazione = "sessuologo"):
        super().__init__(nome, eta)
        self.specializzazione = specializzazione
        
    def supporta_team(self):
        return f"{self.nome} supporta il team come {self.specializzazione}."
