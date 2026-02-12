"""Andiamo a creare un sistema ripetibile che simuli un teatro:

Classe Base: Posto
Attributi privati:
_numero (intero): il numero del posto.
_fila (stringa): la fila in cui si trova il posto.
_occupato (booleano): stato del posto, se è occupato (True) o libero (False).
Metodi:
__init__(numero, fila): inizializza il posto impostando _occupato a False.
prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
Getter: per recuperare il numero, la fila e lo stato (occupato/libero).

Classi Derivate
PostoVIP:
Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come “Accesso al lounge”, “Servizio in posto”).
Metodi:
Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l’attivazione dei servizi extra.
PostoStandard:
Attributi aggiuntivi: costo
Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
Metodi:
Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
Classe Teatro
Attributi:
_posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
Metodi:
aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
stampa_posti_occupati(): stampa tutti i posti che risultano occupati."""

# Implementazione del sistema del teatro con classi e polimorfismo
# classe Posto
class Posto():
    def __init__(self, numero, fila):
        self._numero = numero
        self._fila = fila
        self._occupato = False
    
    # metodo per prenotare il posto
    def prenota(self):
        if not self._occupato:
            self._occupato = True
            print(f"Posto {self._numero} in fila {self._fila} prenotato con successo.")
            return True # Ritorna True se l'operazione va a buon fine
        else:
            print(f"Il posto {self._numero} in fila {self._fila} è già occupato.")
            return False
    
    # metodo per liberare il posto
    def libera(self):
        if self._occupato:
            self._occupato = False
            print(f"Posto {self._numero} in fila {self._fila} liberato con successo.")
        else:
            print(f"Il posto {self._numero} in fila {self._fila} non era prenotato.")
    
    # getter per numero, fila e stato
    def __str__(self):
        return f"Posto {self._numero} in fila {self._fila} - {'Occupato' if self._occupato else 'Libero'}" 

# classi derivate
class PostoVIP(Posto):
    servizi_extra = ["Accesso al lounge", "Servizio in posto"]
    
    def prenota(self):
        if super().prenota(): # Esegue il codice extra solo se la prenotazione riesce
            print(f"Servizi extra attivati: {', '.join(self.servizi_extra)}")
            return True
        return False

class PostoStandard(Posto):
    prenotazione_online = 12.99
    
    def prenota(self):
        if super().prenota():
            print(f"Il costo della prenotazione online è: {self.prenotazione_online}€")
            return True
        return False


class Teatro():
    def __init__(self):
        self._posti = {}
    
    def aggiungi_posto(self, posto):
        # Uso una chiave univoca (numero, fila)
        self._posti[(posto._numero, posto._fila)] = posto
        print("Posto aggiunto al sistema.")
    
    def prenota_posto(self, numero, fila):
        # Cerco direttamente nel dizionario
        posto = self._posti.get((numero, fila))
        if posto:
            posto.prenota()
        else:
            print(f"Errore: Il posto {numero} in fila {fila} non esiste nel sistema.")
    
    def stampa_posti_occupati(self):
        print("\nPosti occupati:")
        trovato = False
        for p in self._posti.values():
            if p._occupato:
                trovato = True
                yield str(p)
        if not trovato:
            yield "Nessun posto occupato al momento."

# Funzioni di utilità
def check_numero(numero):
    if numero.isdigit():
        return int(numero)
    else:
        print("Errore: Il numero deve essere un intero.")
        return False

def menu():
    teatro_OBJ = Teatro() 

    while True:
        print("\n--- Benvenuto al teatro dei morti viventi! ---")
        r = input("0. Esci\n1. Aggiungi posto al sistema\n2. Prenota posto\n3. Stampa posti occupati\nScegli: ")
        
        match r:
            case "0":
                print("Uscita in corso...")
                break
            
            case "1":
                n = input("Numero posto: ")
                n_int = check_numero(n)
                if n_int is False: continue
                
                f = input("Fila posto: ")
                t = input("Il posto è VIP? (s/n): ")
                
                # Creazione oggetto
                if t.lower() == "s":
                    nuovo_posto = PostoVIP(n_int, f)
                else:
                    nuovo_posto = PostoStandard(n_int, f)
                

                teatro_OBJ.aggiungi_posto(nuovo_posto)
                
            case "2":
                n = input("Numero da prenotare: ")
                n_int = check_numero(n)
                if n_int is False: continue
                
                f = input("Fila da prenotare: ")
                teatro_OBJ.prenota_posto(n_int, f)
            
            case "3":
                # Consumo il generatore
                for riga in teatro_OBJ.stampa_posti_occupati():
                    print(riga)
            
            case _:
                print("Opzione non valida.")

if __name__ == "__main__":
    menu()