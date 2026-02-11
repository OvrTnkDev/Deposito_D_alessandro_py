"""L'obiettivo è utilizzare l'incapsulamento per prevenire accessi non autorizzati o modifiche inappropriate al saldo del conto.

Classe ContoBancario:
Attributi privati:
__titolare (stringa che rappresenta il nome del titolare del conto)
__saldo (decimale che rappresenta il saldo del conto)
Metodi pubblici:
deposita(importo): aggiunge un importo al saldo solo se l'importo è positivo.
preleva(importo): sottrae un importo dal saldo solo se ci sono fondi sufficienti e l'importo è positivo.
visualizza_saldo(): restituisce il saldo corrente senza permettere la sua modifica diretta.
Gestione dei Metodi e Sicurezza:
I metodi deposita e preleva devono controllare che gli importi siano validi (e.g., non negativi).
Aggiungere metodi "getter" e "setter" per gli attributi come _titolare, applicando validazioni appropriate (e.g., il titolare deve essere una stringa non vuota)."""
from termcolor import colored as cl

class ContoBancario():
    def __init__(self, titolare, ruolo, saldo_iniziale=0):
        if not titolare.strip():
            print(cl("Il nome del titolare non può essere vuoto.", "red"))
            return
        else:
            self.__titolare = titolare.strip()
            self.__ruolo = ruolo.lower()
            self.__saldo = saldo_iniziale
        
    def controlla_ruolo(self):
        if self.__ruolo == "utente":
            return True
        else:
            return False
        
    def get_importo(self):
        return self.__saldo
        
    def deposita(self, importo):
        if not self.controlla_ruolo():
            print(cl("Solo gli utenti possono effettuare depositi.", "red"))
            print(cl("Ti ho CatFishato!", "red", attrs=["bold"]))
            return
        if importo > 0:
            self.__saldo += importo
            print(cl(f"Deposito di {importo} effettuato. Saldo attuale: {self.__saldo}$.", "green"))
        else:
            print(cl("L'importo del deposito deve essere positivo.", "red"))
            
    def preleva(self, importo):
        if not self.controlla_ruolo():
            print(cl("Solo gli utenti possono effettuare prelievi.", "red"))
            print(cl("Ti ho CatFishato!", "red", attrs=["bold"]))
            return
        if importo > 0:
            if self.__saldo >= importo:
                self.__saldo -= importo
                print(cl(f"Prelievo di {importo}$ effettuato. Saldo attuale: {self.__saldo}$.", "green"))
            else:
                print(cl("Fondi insufficienti per effettuare il prelievo.", "red"))
        else:
            print(cl("L'importo del prelievo deve essere positivo.", "red"))
    
    def visualizza_saldo(self):
        print(cl(f"Saldo attuale: {self.__saldo}$", "blue"))
        
        
class Utente(ContoBancario):
    def __init__(self, titolare, saldo_iniziale=0):
        super().__init__(titolare, "utente", saldo_iniziale)


class Admin(ContoBancario):
    def __init__(self, titolare, saldo_iniziale=0):
        super().__init__(titolare, "admin", saldo_iniziale)
