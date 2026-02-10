"""Il sistema deve includere una classe Pacco con: codice (stringa), peso (numero)
e stato (es. "in magazzino", "in consegna", "consegnato"), con un metodo per mostrare le info e un metodo per cambiare stato.

Deve esserci una classe Magazzino che contiene una lista (o dizionario) di pacchi 
e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato.

Deve esserci infine una classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”, 
segnare un pacco come “consegnato” e calcolare il peso totale dei pacchi ancora non consegnati.

Nel programma principale crea almeno 5 pacchi, inseriscili nel magazzino, 
cambia lo stato di alcuni pacchi (almeno una consegna avviata e una consegna completata) 
e stampa: elenco pacchi “in magazzino”, elenco pacchi “in consegna” e il peso totale dei pacchi non ancora consegnati."""

# Creazione della classe Pacco con codice, peso e stato, e metodi per mostrare info e cambiare stato
class Pacco():
    def __init__(self,codice:str, peso:float, stato:str):
        self.codice = codice
        #peso arrotondato a 2 decimali
        self.peso = round(peso, 2)
        self.stato = stato

def __str__(self):
    return f"Pacco {self.codice}: peso {self.peso} kg, stato '{self.stato}'"

def cambia_stato(self, n_stato:str):
    self.stato = n_stato
    print(f"Il pacco {self.codice} è ora '{self.stato}'")

"""Creazione della classe Magazzino che contiene una lista di pacchi 
e permette di aggiungere un pacco, cercarlo per codice, e mostrare tutti i pacchi in un certo stato"""
class Magazzino():
    def __init__(self):
        self.pacchi = {}
        
    # aggiunge un pacco al magazzino, usando il codice come chiave
    def agg_pacco(self, pacco):
        self.pacchi[pacco.codice] = pacco
        print(f"Pacco {pacco.codice} aggiunto al magazzino.")
    
    # cerca un pacco per codice e lo restituisce, altrimenti restituisce un messaggio di errore
    def cerca_pacco(self, codice:str):
        if codice in self.pacchi:
            return self.pacchi[codice]
        else:
            print(f"Pacco con codice {codice} non trovato.")
            return "Pacco non trovato"
        
    # mostra tutti i pacchi in un certo stato
    def stato_pacco(self, stato:str):
        for pacco in self.pacchi.values():
            if pacco.stato == stato:
                print(pacco)
            else:
                print(f"Nessun pacco con stato '{stato}' trovato.")

"""Creazione della classe GestorePacchi che usa il magazzino per mettere un pacco “in consegna”"""
class GestorePacchi():
    # il costruttore prende in input un magazzino
    def __init__(self, magazzino):
        self.magazzino = magazzino
        
    def c_pacco(self, codice:str):
        # sfrutto il metodo cerca_pacco del magazzino per trovare il pacco e cambiarne lo stato in "in consegna"
        pacco = self.magazzino.cerca_pacco(codice)
        # se il pacco è stato trovato e il suo stato è "in magazzino", lo cambio in "in consegna"
        if pacco != "Pacco non trovato" and pacco.stato == "in magazzino":
            pacco.cambia_stato("in consegna")
        # se il pacco è stato trovato e il suo stato è "in consegna", lo cambio in "consegnato"
        elif pacco != "Pacco non trovato" and pacco.stato == "in consegna":
            pacco.cambia_stato("consegnato")
        else:
            print(f"Il pacco {codice} non è in magazzino, non può essere messo in consegna.")
        
        # calcolo il peso totale dei pacchi ancora non consegnati.
    def peso_totale(self):
        peso_totale = 0
        for pacco in self.magazzino.pacchi.values():
            if pacco.stato == "in magazzino":
                peso_totale += pacco.peso
        return peso_totale

# programma principale
def main():
    magazzino_OBJ = Magazzino()
    gestore_OBJ = GestorePacchi(magazzino_OBJ)
    while True:
        r = input("\nBenvenuto nel sistema di gestione pacchi!\n" + 
                  "Scegli un'opzione:\n" +
                  "1. Aggiungi pacco\n" +
                  "2. Cerca pacco\n" +
                  "3. Cambia stato pacco\n" +
                  "4. Mostra pacchi per stato\n" +
                  "5. Calcola peso totale pacchi non consegnati\n" +
                  "6. Esci\n" +
                  "Scegli un'opzione: ")

        match r:
            case "1":
                c = input("Inserisci il codice del pacco: ")
                while True:
                    p = float(input("Inserisci il peso del pacco (kg): "))
                    if p < 0:
                        print("Peso non valido. Inserisci un numero positivo.")
                        continue
                    else:
                        break
                pacco_OBJ = Pacco(c, p, "in magazzino")
                magazzino_OBJ.agg_pacco(pacco_OBJ)
            case "2":
                c = input("inserisci il codice del pacco da cercare: ")
                print(magazzino_OBJ.cerca_pacco(c))
            case "3":
                c = input("inserisci il codice del pacco da cambiare stato: ")
                gestore_OBJ.c_pacco(c)
            case "4":
                s = input("inserisci lo stato dei pacchi da mostrare (in magazzino, in consegna, consegnato): ")
                magazzino_OBJ.stato_pacco(s)
            case "5":
                print(f"Il peso totale dei pacchi non consegnati è: {gestore_OBJ.peso_totale()} kg")
            case "6":
                print("Uscita dal sistema...")
                exit()
            case _:
                print("Scelta non valida. Per favore, inserisci un numero da 1 a 6.")
                continue


if __name__ == "__main__":
    main()