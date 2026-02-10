#classi: Negozio, Utente (fatto)
#dizionario: inventario (fatto)
#chiedere all'utente all'inizio se vuole essere un negozio o un cliente
#se è un negozio, chiedere il nome del negozio e i prodotti che vende
#se è un cliente, chiedere il nome del cliente e i prodotti che vuole acquistare

"""Esercizio: Sistema di Gestione Negozio

Lo scopo di questo esercizio è implementare un sistema di gestione per un negozio che deve interagire con clienti,
gestire l'inventario e permettere agli amministratori di supervisionare le operazioni.
Il sistema sarà strutturato in tre parti principali:
Gestione Clienti:
I clienti possono visualizzare gli articoli disponibili in inventario.
I clienti possono selezionare e acquistare articoli dall'inventario.
Il sistema tiene traccia degli acquisti dei clienti.
Gestione dell'Inventario:
Gli articoli in magazzino sono elencati con il nome, il prezzo e la quantità.
È possibile aggiungere nuovi articoli all'inventario.
Gli articoli possono essere rimossi o aggiornati (ad es., cambiare prezzo o quantità).
Amministrazione:
l'analisi del negozio da parte degli amministratori.

Gli amministratori possono visualizzare lo stato corrente dell'inventario.
Il sistema tiene traccia dei guadagni totali.
Puoi pre inserire gli amministratori non i clienti
Il sistema dovrebbe permettere di simulare un'interazione base tra il cliente e il negozio dopo un login e una registrazione,
nonché fornire gli strumenti necessari per la manutenzione e l'analisi del negozio da parte degli amministratori."""

# Creazione dell'inventario iniziale tramite dizionario hardcoded
"""inventario = {"elettronica":{"telefono": {"prezzo": 500, "quantità": 10},
                            "laptop": {"prezzo": 1000, "quantità": 5}},
                "abbigliamento":{"maglietta": {"prezzo": 20, "quantità": 50},
                                "jeans": {"prezzo": 40, "quantità": 30}},
                "games":{"videogioco1": {"prezzo": 60, "quantità": 20},
                        "videogioco2": {"prezzo": 70, "quantità": 15}}}"""

# Creazione delle classi Utente
class Utente():
    #creo password globali fittizie per amministratore e cliente
    _password_admin = "admin123"
    _password_utente = "utente123"
    #creo il costruttore della classe che prende in input nome, ruolo e password
    def __init__ (self, nome, ruolo, password):
        self.nome = nome
        self.ruolo = ruolo
        self.password = password
    #creo i metodi di login per amministratore e cliente che confrontano la password inserita con quella predefinita
    def login_admin(self):
        if self.password == self._password_admin:
            print(f"Benvenuto {self.nome}, sei loggato come {self.ruolo}.")
            return True
        else:
            print("Password errata. Accesso negato.")
            return False

    def login_utente(self):
        if self.password == self._password_utente:
            print(f"Benvenuto {self.nome}, sei loggato come {self.ruolo}.")
            return True
        else:
            print("Password errata. Accesso negato.")
            return False
# creazione della classe negozio
class Negozio():
    inventario = {}
    carrello = {}
    
    #creo il costruttore della classe che prende in input nome, ruolo e inventario (opzionale)
    def __init__(self, nome, ruolo):
        self.nome = nome
        self.ruolo = ruolo
            
    def visualizza_inventario(self):
        for cat, prod in self.inventario.items():
            print(f"Categoria: {cat}")
            for nome, info in prod.items():
                print(f"  - {nome}: Prezzo: {info['prezzo']}€, Quantità: {info['quantità']}")
    
    def acquista_prodotto(self, categoria, prodotto, quantità):
        #verifico se la categoria e il prodotto esistono nell'inventario
        if categoria in self.inventario and prodotto in self.inventario[categoria]:
            #verifico se la quantità richiesta è disponibile
            if self.inventario[categoria][prodotto]["quantità"] >= quantità:
                #calcolo il prezzo totale dell'acquisto e lo aggiungo al carrello del cliente, aggiornando l'inventario di conseguenza
                prezzo_totale = self.inventario[categoria][prodotto]["prezzo"] * quantità
                self.carrello[prodotto] = {"prezzo": prezzo_totale, "quantità": quantità}
                self.inventario[categoria][prodotto]["quantità"] -= quantità
                print(f"Hai aggiunto {quantità} {prodotto} al carrello. Prezzo totale: {prezzo_totale}€")
                
            else:
                print("Quantità richiesta non disponibile.")
                
        else:
            print("Prodotto non trovato nell'inventario.")
            
    def aggiungi_prodotto(self, categoria, prodotto, prezzo, quantità):
        if categoria not in self.inventario:
            self.inventario[categoria] = {}

        self.inventario[categoria][prodotto] = {"prezzo": prezzo, "quantità": quantità}
        
    def controllo_guadagni(self):
        guadagni_totali = sum(item["prezzo"] for item in self.carrello.values())
        print(f"Guadagni totali: {guadagni_totali}€")

# Funzione per gestire l'interazione del cliente
def cliente():
    while True:
            n = input("Inserisci il tuo nome: ")
            p = input("Inserisci la tua password: ")
            cliente = Utente(n, "cliente", p)
            if not cliente.login_utente():
                break
            else:
                negozio_OBJ = Negozio(n, "cliente")
                while True:
                    r = input("\n0: Visualizza inventario\n1: Acquista prodotto\n2: Esci\n3: Esci dal menu utente\nScegli un'opzione: ")
                    match r:
                        case "0":
                            print("\nInventario disponibile:")
                            negozio_OBJ.visualizza_inventario()
                        case "1":
                            categoria = input("Inserisci la categoria del prodotto: ")
                            prodotto = input("Inserisci il nome del prodotto: ")
                            quantità = int(input("Inserisci la quantità: "))
                            negozio_OBJ.acquista_prodotto(categoria, prodotto, quantità)
                        case "2":
                            print("Uscita dal sistema...")
                            exit()
                        case "3":
                            print("Uscita e logout...")
                            # strategia per uscire e tornare al menu principale senza chiudere il programma
                            return
                        case _:
                            print("Scelta non valida. Per favore, inserisci '0', '1' o '2'.")
                            continue

# Funzione per gestire l'interazione dell'amministratore
def amministratore():
    while True:
        n = input("Inserisci il tuo nome: ")
        p = input("Inserisci la tua password: ")
        admin = Utente(n, "amministratore", p)
        if not admin.login_admin():
            break
        else:
            negozio_OBJ = Negozio(n, "amministratore")
            while True:
                r = input("\n0: Visualizza inventario\n1: Aggiungi prodotto\n2: Controllo guadagni\n3: Esci\n4: Esci dal menu amministratore\nScegli un'opzione: ")
                match r:
                    case "0":
                        print("\nInventario disponibile:")
                        negozio_OBJ.visualizza_inventario()
                    case "1":
                        categoria = input("Inserisci la categoria del prodotto: ")
                        prodotto = input("Inserisci il nome del prodotto: ")
                        prezzo = float(input("Inserisci il prezzo del prodotto: "))
                        quantità = int(input("Inserisci la quantità del prodotto: "))
                        negozio_OBJ.aggiungi_prodotto(categoria, prodotto, prezzo, quantità)
                    case "2":
                        print("Guadagni attuali:")
                        negozio_OBJ.controllo_guadagni()
                    case "3":
                        print("Uscita dal sistema...")
                        exit()
                    case "4":
                        print("Uscita e logout...")
                        # strategia per uscire e tornare al menu principale senza chiudere il programma
                        return
                    case _:
                        print("Scelta non valida. Per favore, inserisci '0', '1', '2' o '4'.")
                        continue
        
# Funzione principale per gestire l'interazione iniziale
def main():
    while True:
        print("Benvenuto nel sistema di gestione del negozio!")
        r = (input("Sei un amministratore, un cliente o vuoi uscire? (a/c/q): ")).lower()
        
        match r:
            case "a":
                amministratore()
                continue
                
            case "c":
                cliente()
                continue
                    
            case "q":
                print("Grazie per aver utilizzato il sistema di gestione del negozio. Arrivederci!")
                exit()
                
            case _:
                print("Scelta non valida. Per favore, inserisci 'a' per amministratore, 'c' per cliente o 'q' per uscire.")
                continue

# Avvio del programma
if __name__ == "__main__":
    main()