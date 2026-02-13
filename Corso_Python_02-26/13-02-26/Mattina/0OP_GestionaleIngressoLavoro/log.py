from turni import Turno

# creazione di classe accesso e classe log per gestire i log di entrata e uscita dei dipendenti
class Accesso(Turno):
    def __init__(self, nome, ruolo, orario, tipo):
      super().__init__(nome, ruolo, orario, None)
      self.orario = orario
      self.tipo = tipo  # tipo può essere "entrata" o "uscita"
      
    def controllo_accesso(self):
        # logica di controllo accesso, ad esempio verificare se il dipendente ha un badge valido e se è autorizzato a entrare in quel momento
        print(f"Controllo accesso per {self.nome} - Tipo: {self.tipo} - Orario: {self.orario}")

# creazione di classi e funzioni per gestire i log di entrata e uscita dei dipendenti
class Log():
    def __init__(self):
        self.entrate = {}
        self.uscite = {}
    
    def registra_entrata(self, accesso):
        self.entrate[accesso.nome] = accesso.orario
        print(f"Registrata entrata di {accesso.nome} alle {accesso.orario}")
    
    def registra_uscita(self, accesso):
        self.uscite[accesso.nome] = accesso.orario
        print(f"Registrata uscita di {accesso.nome} alle {accesso.orario}")