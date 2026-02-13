from dipendenti import Badge

# creazione di classe turno per gestire i turni di lavoro dei dipendenti
class Turno(Badge):
    def __init__(self, nome, ruolo, orario_inizio, orario_fine):
        super().__init__(nome, ruolo)
        self.orario_inizio = orario_inizio
        self.orario_fine = orario_fine
    
    # polimorfismo: il metodo __str__ è sovrascritto per fornire una rappresentazione stringa specifica per la classe Turno
    def __str__(self):
        return super().__str__() + f" - Turno: {self.orario_inizio} - {self.orario_fine}"
      
    def salva_turno(self):
        # salva il turno in un database simulato (un dizionario)
        print(f"Turno per {self.nome} salvato: {self.orario_inizio} - {self.orario_fine}")